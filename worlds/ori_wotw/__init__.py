"""AP world for Ori and the Will of the Wisps."""

# TODO Relics ? Black market ?
# TODO fix the in-game location counter
# TODO rename MultiWorld to mw and use new world API for regions
# TODO location groups (as a set)
# TODO Add relics to slot_data and client implementation


from typing import Any
from collections import Counter

from .Rules import (set_moki_rules, set_gorlek_rules, set_gorlek_glitched_rules, set_kii_rules,
                    set_kii_glitched_rules, set_unsafe_rules, set_unsafe_glitched_rules)
from .AdditionalRules import combat_rules, glitch_rules, unreachable_rules
from .Items import item_table
from .Items_Icons import get_item_iconpath
from .Locations import loc_table
from .Quests import quest_table
from .LocationGroups import loc_sets, location_regions
from .Events import event_table
from .Regions import region_table
from .Entrances import entrance_table
from .Refills import refill_events
from .Options import WotWOptions, option_groups, LogicDifficulty, Quests
from .SpawnItems import spawn_items, spawn_names
from .Presets import options_presets
from .ItemGroups import item_groups
from .RulesFunctions import get_max, get_refill

from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule, set_rule
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, LocationProgressType, CollectionState


class WotWWeb(WebWorld):
    theme = "ocean"  # TODO documentation
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Ori and the Will of the Wisps randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Satisha"]
    )]
    options_presets = options_presets
    option_groups = option_groups
    bug_report_page = "https://discord.com/channels/731205301247803413/1272952565843103765"


class WotWWorld(World):
    """Ori and the Will of the Wisps is a 2D Metroidvania;
    The sequel to Ori and the blind forest, a platform game emphasizing exploration, collecting items and upgrades, and backtracking to previously inaccessible areas.
    The player controls the titular Ori, a white guardian spirit.
    """
    game = "Ori and the Will of the Wisps"
    web = WotWWeb()

    item_name_to_id = {name: data[2] for name, data in item_table.items()}
    location_name_to_id = loc_table

    item_name_groups = item_groups

    options_dataclass = WotWOptions
    options: WotWOptions
    explicit_indirect_conditions = False  # TODO remove

    required_client_version = (0, 5, 0)

    def __init__(self, multiworld, player) -> None:
        super(WotWWorld, self).__init__(multiworld, player)
        self.relic_areas: list[str] = []  # Store which areas contain a relic
        self.empty_locations: list[str] = []  # Excluded locations, for now hold a Nothing item

    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)
        if change and item.name in ("Health Fragment", "Energy Fragment"):  # TODO Wisps ? See if events are collected as well
            state.wotw_max_resources[self.player] = get_max(state, self.player)
            state.wotw_refill_amount[self.player] = get_refill(state, self.player)
        return change

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        if change and item.name in ("Health Fragment", "Energy Fragment"):
            state.wotw_max_resources[self.player] = get_max(state, self.player)
            state.wotw_refill_amount[self.player] = get_refill(state, self.player)
        return change

    def generate_early(self) -> None:
        options = self.options
        # Options checking
        if options.open_mode:
            options.no_rain.value = True

        # Selection of a random goal
        if "random" in options.goal:
            possible_goals = list(options.goal.value)
            possible_goals.remove("random")
            selected_goal: list = []
            if not possible_goals:  # Only random selected, choose among all goals
                possible_goals = ["trees", "wisps", "quests"]
            # Select a goal at random among the selected ones
            selected_goal.append(self.multiworld.random.choice(possible_goals))
            options.goal.value = set(selected_goal)


        # Construct the excluded locations list
        if options.glades_done:
            self.empty_locations += loc_sets["Rebuild"].copy()
        if options.no_trials:
            self.empty_locations += loc_sets["Trials"].copy()
        if options.qol or options.quests == Quests.option_none:
            self.empty_locations += loc_sets["QOL"].copy()
        if options.quests != Quests.option_all:
            self.empty_locations += loc_sets["HandToHand"].copy()
        if options.quests == Quests.option_none:
            self.empty_locations += loc_sets["Quests"].copy()
        else:
            self.empty_locations += ["GladesTown.FamilyReunionKey"]  # TODO remove when fixed

    def create_regions(self) -> None:
        world = self.multiworld
        player = self.player
        options = self.options

        for region_name in region_table:
            region = Region(region_name, player, world)
            world.regions.append(region)

        menu_region = Region("Menu", player, world)
        world.regions.append(menu_region)

        spawn_name = spawn_names[options.spawn]
        spawn_region = world.get_region(spawn_name, player)  # Links menu with spawn point
        menu_region.connect(spawn_region)

        menu_region.connect(world.get_region("HeaderStates", player))

        for loc_name in loc_table.keys():  # Create regions on locations
            region = Region(loc_name, player, world)
            world.regions.append(region)
            region.locations.append(WotWLocation(player, loc_name, self.location_name_to_id[loc_name], region))
        for quest_name in quest_table:  # Quests are locations that have to be tracked like events
            event_name = quest_name + ".quest"
            event_region = Region(event_name, player, world)  # Region that holds the event item
            world.regions.append(event_region)
            event = WotWLocation(player, event_name, None, event_region)
            event.show_in_spoiler = False
            event.place_locked_item(self.create_event_item(quest_name))
            event_region.locations.append(event)
            base_region = world.get_region(quest_name, player)  # Region that holds the location
            base_region.connect(event_region)  # Connect the event region to the base region

        for event in event_table:  # Various events
            self.create_event(event)
        for event in refill_events:  # Tracks the refills that are accessible
            self.create_event(event)

        for entrance_name in entrance_table:  # Creates and connects the entrances
            (parent, connected) = entrance_name.split("_to_")
            parent_region = world.get_region(parent, player)
            connected_region = world.get_region(connected, player)
            entrance = parent_region.create_exit(entrance_name)
            entrance.access_rule = lambda state: False
            entrance.connect(connected_region)

        region = Region("Victory", player, world)  # Victory event
        ev = WotWLocation(player, "Victory", None, region)
        ev.place_locked_item(WotWItem("Victory", ItemClassification.progression, None, player))
        world.regions.append(region)
        region.locations.append(ev)

        world.completion_condition[player] = lambda state: state.has("Victory", player)

    def create_event(self, event: str) -> None:
        """Create an event, place the item and attach it to an event region (all with the same name)."""
        event_region = Region(event, self.player, self.multiworld)
        event_location = WotWLocation(self.player, event, None, event_region)
        event_location.show_in_spoiler = False
        event_location.place_locked_item(self.create_event_item(event))
        self.multiworld.regions.append(event_region)
        event_region.locations.append(event_location)

    def create_item(self, name: str) -> "WotWItem":
        return WotWItem(name, item_table[name][1], item_table[name][2], player=self.player)

    def create_items(self) -> None:
        world = self.multiworld
        player = self.player
        options = self.options

        skipped_items: list[str] = []  # Remove one instance of the item
        removed_items: list[str] = []  # Remove all instances of the item

        # TODO Check if random must be taken from mw or world
        for item in spawn_items(world, options.spawn.value, options.difficulty.value):  # Staring items
            world.push_precollected(self.create_item(item))
            skipped_items.append(item)

        for item, count in options.start_inventory.value.items():
            for _ in range(count):
                skipped_items.append(item)

        if options.sword:
            world.push_precollected(self.create_item("Sword"))
            removed_items.append("Sword")

        if not options.tp:
            for item in item_groups["teleporters"]:
                removed_items.append(item)

        if not options.extratp:
            for item in item_groups["extra_tp"]:
                removed_items.append(item)

        if not options.bonus:
            for item in item_groups["bonus"]:
                removed_items.append(item)

        if not options.extra_bonus:
            for item in item_groups["bonus+"]:
                removed_items.append(item)

        if not options.skill_upgrade:
            for item in item_groups["skill_upgrades"]:
                removed_items.append(item)

        if options.glades_done:
            removed_items.append("Gorlek Ore")

        if options.no_ks:
            removed_items.append("Keystone")

        if options.vanilla_shop_upgrades:
            shop_items = {"OpherShop.ExplodingSpike": "Exploding Spear",
                          "OpherShop.ShockSmash": "Hammer Shockwave",
                          "OpherShop.StaticStar": "Static Shuriken",
                          "OpherShop.ChargeBlaze": "Charge Blaze",
                          "OpherShop.RapidSentry": "Rapid Sentry",
                          "OpherShop.WaterBreath": "Water Breath",
                          "TwillenShop.Overcharge": "Overcharge",
                          "TwillenShop.TripleJump": "Triple Jump",
                          "TwillenShop.Wingclip": "Wingclip",
                          "TwillenShop.Swap": "Swap",
                          "TwillenShop.LightHarvest": "Light Harvest",
                          "TwillenShop.Vitality": "Vitality",
                          "TwillenShop.Energy": "Energy (Shard)",
                          "TwillenShop.Finesse": "Finesse"}
            for location, item in shop_items.items():
                loc = world.get_location(location, player)
                loc.place_locked_item(self.create_item(item))
                removed_items.append(item)

        if options.launch_on_seir:
            world.get_location("WindtornRuins.Seir", player).place_locked_item(self.create_item("Launch"))
            removed_items.append("Launch")

        for location in self.empty_locations:  # TODO temporary workaround
            loc = world.get_location(location, player)
            loc.place_locked_item(self.create_item("Nothing"))

        counter = Counter(skipped_items)
        pool: list[WotWItem] = []

        for item, data in item_table.items():
            if item in removed_items:
                count = -counter[item]
            else:
                count = data[0] - counter[item]
            if count <= 0:  # This can happen with starting inventory
                count = 0

            for _ in range(count):
                pool.append(self.create_item(item))

        extras = len(world.get_unfilled_locations(player=self.player)) - len(pool)
        for _ in range(extras):
            pool.append(self.create_item(self.get_filler_item_name()))

        world.itempool += pool

        if options.difficulty == LogicDifficulty.option_moki:
            # Exclude a location that is inaccessible in the lowest difficulty.
            skipped_loc = world.get_location("WestPools.BurrowOre", player)
            skipped_loc.progress_type = LocationProgressType.EXCLUDED

        if "relics" in options.goal:  # Put the relics at random places in the areas
            remaining_areas: list[str] = [
                "Marsh",
                "Burrows",
                "Hollow",
                "Glades",
                "Wellspring",
                "Woods",
                "Reach",
                "Pools",
                "Depths",
                "Wastes",
                "Willow",
            ]
            for _ in range(options.relic_count.value):
                area: str = self.random.choice(remaining_areas)
                remaining_areas.remove(area)
                self.relic_areas.append(area)

                relic_location: str = self.random.choice(location_regions[area])
                while relic_location in self.excluded_locations:  # Reroll if the location is excluded
                    relic_location = self.random.choice(location_regions[area])
                self.get_location(relic_location).place_locked_item(self.create_item("Relic"))

    def create_event_item(self, event: str) -> "WotWItem":
        return WotWItem(event, ItemClassification.progression, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(["50 Spirit Light", "100 Spirit Light"])

    def set_rules(self) -> None:
        world = self.multiworld
        player = self.player
        options = self.options
        menu = world.get_region("Menu", player)
        difficulty = options.difficulty

        # Add the basic rules.
        set_moki_rules(world, player, options)
        combat_rules(world, player, options)
        glitch_rules(world, player, options)
        unreachable_rules(world, player, options)

        # Add rules depending on the logic difficulty.
        if difficulty == LogicDifficulty.option_moki:
            # Extra rule for a location that is inaccessible in the lowest difficulty.
            add_rule(world.get_entrance("WestPools.Teleporter_to_WestPools.BurrowOre", player),
                     lambda state: state.has_all(("Burrow", "Clean Water", "Water Dash"), player), "or")
        if difficulty >= LogicDifficulty.option_gorlek:
            set_gorlek_rules(world, player, options)
            if options.glitches:
                set_gorlek_glitched_rules(world, player, options)
        if difficulty >= LogicDifficulty.option_kii:
            set_kii_rules(world, player, options)
            if options.glitches:
                set_kii_glitched_rules(world, player, options)
        if difficulty == LogicDifficulty.option_unsafe:
            set_unsafe_rules(world, player, options)
            if options.glitches:
                set_unsafe_glitched_rules(world, player, options)

        # Add victory condition
        victory_conn = world.get_region("WillowsEnd.Upper", player).connect(world.get_region("Victory", player))
        set_rule(victory_conn, lambda s: s.has_any(("Sword", "Hammer"), player)
                         and s.has_all(("Double Jump", "Dash", "Bash", "Grapple", "Glide", "Burrow", "Launch"), player))

        if "trees" in options.goal:
            add_rule(victory_conn, lambda s: all([s.can_reach_region(tree, player)
                          for tree in ["MarshSpawn.RegenTree",
                                       "MarshSpawn.DamageTree",
                                       "HowlsDen.SwordTree",
                                       "HowlsDen.DoubleJumpTree",
                                       "MarshPastOpher.BowTree",
                                       "WestHollow.DashTree",
                                       "EastHollow.BashTree",
                                       "GladesTown.DamageTree",
                                       "InnerWellspring.GrappleTree",
                                       "UpperPools.SwimDashTree",
                                       "UpperReach.LightBurstTree",
                                       "LowerDepths.FlashTree",
                                       "LowerWastes.BurrowTree",
                                       "WeepingRidge.LaunchTree",
                                       ]
                          ])
                     )

        if "wisps" in options.goal:
            add_rule(victory_conn, lambda s: s.has_all(("EastHollow.ForestsVoice", "LowerReach.ForestsMemory",
                                                        "UpperDepths.ForestsEyes", "WestPools.ForestsStrength",
                                                        "WindtornRuins.Seir"), player)
                     )

        if "quests" in options.goal:
            quest_list: list[str] = loc_sets["ExtraQuests"].copy()
            if options.quests == Quests.option_no_hand:
                quest_list += loc_sets["Quests"].copy()
            elif options.quests == Quests.option_all:
                quest_list += loc_sets["Quests"].copy() + loc_sets["HandToHand"].copy()
            if not options.glades_done:
                quest_list += loc_sets["Rebuild"].copy()
            if not options.qol and options.quests != Quests.option_none:
                quest_list += loc_sets["QOL"].copy()
            add_rule(victory_conn, lambda s: s.has_all((quests for quests in quest_list), player))

        if "relics" in options.goal:
            add_rule(victory_conn, lambda s: s.count("Relics", player) >= options.relic_count.value)

        def try_connect(region_in: Region, region_out: Region, connection: str | None = None, rule=None) -> None:
            """Create the region connection if it doesn't already exist."""
            if connection is None:
                connection = f"{region_in.name}_to_{region_out.name}"
            if not world.regions.entrance_cache[player].get(connection):
                region_in.connect(region_out, connection, rule)

        # Rules for specific options
        if options.qol:
            try_connect(menu, world.get_region("GladesTown.TuleySpawned", player))
            world.get_region("WoodsEntry.LastTreeBranch", player).connect(
                world.get_region("WoodsEntry.TreeSeed", player))
        if options.better_spawn:
            try_connect(menu, world.get_region("MarshSpawn.HowlBurnt", player))
            try_connect(menu, world.get_region("HowlsDen.BoneBarrier", player))
            try_connect(menu, world.get_region("EastPools.EntryLever", player))
            try_connect(menu, world.get_region("UpperWastes.LeverDoor", player))

        if "Everything" in options.no_combat or "Bosses" in options.no_combat:
            for entrance in ("HeaderStates_to_SkipKwolok",
                             "HeaderStates_to_SkipMora1",
                             "HeaderStates_to_SkipMora2"):
                set_rule(world.get_entrance(entrance, player), lambda s: True)
        else:  # Connect these events when the seed is completed, to make them reachable.
            set_rule(world.get_entrance("HeaderStates_to_SkipKwolok", player),
                     lambda s: s.has("Victory", player))
            set_rule(world.get_entrance("HeaderStates_to_SkipMora1", player),
                     lambda s: s.has("Victory", player))
            set_rule(world.get_entrance("HeaderStates_to_SkipMora2", player),
                     lambda s: s.has("Victory", player))
        if "Everything" in options.no_combat or "Shrines" in options.no_combat:
            for entrance in (
                        "DenShrine_to_HowlsDen.CombatShrineCompleted",
                        "MarshShrine_to_MarshPastOpher.CombatShrineCompleted",
                        "GladesShrine_to_WestGlades.CombatShrineCompleted",
                        "WoodsShrine_to_WoodsMain.CombatShrineCompleted",
                        "DepthsShrine_to_LowerDepths.CombatShrineCompleted"):
                set_rule(world.get_entrance(entrance, player), lambda s: True)

        if options.better_wellspring:
            try_connect(menu, world.get_region("InnerWellspring.TopDoorOpen", player))
        if options.no_ks:
            for event in ("MarshSpawn.KeystoneDoor",
                          "HowlsDen.KeystoneDoor",
                          "MidnightBurrows.KeystoneDoor",
                          "WoodsEntry.KeystoneDoor",
                          "WoodsMain.KeystoneDoor",
                          "LowerReach.KeystoneDoor",
                          "UpperReach.KeystoneDoor",
                          "UpperDepths.EntryKeystoneDoor",
                          "UpperDepths.CentralKeystoneDoor",
                          "UpperPools.KeystoneRoomBubbleFree",
                          "UpperPools.KeystoneDoor",
                          "UpperWastes.KeystoneDoor"):
                try_connect(menu, world.get_region(event, player))
        if options.open_mode:
            for event in ("HowlsDen.BoneBarrier",
                          "MarshSpawn.ToOpherBarrier",
                          "MarshSpawn.TokkBarrier",
                          "MarshSpawn.LogBroken",
                          "MarshSpawn.BurrowsOpen",
                          "MidnightBurrows.HowlsDenShortcut",
                          "MarshPastOpher.EyestoneDoor",
                          "WestHollow.PurpleDoorOpen",
                          "EastHollow.DepthsLever",
                          "GladesTown.GromsWall",
                          "OuterWellspring.EntranceDoorOpen",
                          "InnerWellspring.MiddleDoorsOpen",
                          "InnerWellspring.TopDoorOpen",
                          "EastHollow.DepthsOpen",
                          "LowerReach.Lever",
                          "LowerReach.TPLantern",
                          "LowerReach.RolledSnowball",
                          "LowerReach.EastDoorLantern",
                          "LowerReach.ArenaBeaten",
                          "UpperWastes.LeverDoor",
                          "WindtornRuins.RuinsLever",
                          "WeepingRidge.ElevatorFightCompleted",
                          "EastPools.EntryLever",
                          "EastPools.CentralRoomPurpleWall",
                          "UpperPools.UpperWaterDrained",
                          "UpperPools.ButtonDoorAboveTree",):
                try_connect(menu, world.get_region(event, player))
        if options.no_rain:
            for event in ("HowlsDen.UpperLoopExitBarrier",
                          "HowlsDen.UpperLoopEntranceBarrier",
                          "HowlsDen.RainLifted",):
                try_connect(menu, world.get_region(event, player))
            if not options.better_spawn:
                try_connect(menu, world.get_region("MarshSpawn.HowlBurnt", player))
        if options.glades_done:
            for quest in ("InnerWellspring.BlueMoonSeed",
                          "EastPools.GrassSeed",
                          "UpperDepths.LightcatcherSeed",
                          "UpperReach.SpringSeed",
                          "UpperWastes.FlowersSeed",
                          "WoodsEntry.TreeSeed",
                          "GladesTown.RebuildTheGlades",
                          "GladesTown.RegrowTheGlades",):
                try_connect(menu, world.get_region(quest + ".quest", player))
            for event in ("GladesTown.BuildHuts",
                          "GladesTown.RoofsOverHeads",
                          "GladesTown.OnwardsAndUpwards",
                          "GladesTown.ClearThorns",
                          "GladesTown.CaveEntrance"):
                try_connect(menu, world.get_region(event, player))

        if options.quests != Quests.option_none:  # Open locations locked behind NPCs
            for quest in ("WoodsEntry.LastTreeBranch",
                          "WoodsEntry.DollQI",
                          "GladesTown.FamilyReunionKey"):
                try_connect(menu, world.get_region(quest + ".quest", player))

    def fill_slot_data(self) -> dict[str, Any]:
        # TODO Relics
        world = self.multiworld
        player = self.player
        options = self.options
        logic_difficulty: list[str] = ["Moki", "Gorlek", "Kii", "Unsafe"]
        coord: list[list[int | str]] = [
            [-799, -4310, "MarshSpawn.Main"],
            [-945, -4582, "MidnightBurrows.Teleporter"],
            [-328, -4536, "HowlsDen.Teleporter"],
            [-150, -4238, "EastHollow.Teleporter"],
            [-307, -4153, "GladesTown.Teleporter"],
            [-1308, -3675, "InnerWellspring.Teleporter"],
            [611, -4162, "WoodsEntry.Teleporter"],
            [1083, -4052, "WoodsMain.Teleporter"],
            [-259, -3962, "LowerReach.Teleporter"],
            [513, -4361, "UpperDepths.Teleporter"],
            [-1316, -4153, "EastPools.Teleporter"],
            [-1656, -4171, "WestPools.Teleporter"],
            [1456, -3997, "LowerWastes.WestTP"],
            [1992, -3902, "LowerWastes.EastTP"],
            [2044, -3679, "UpperWastes.NorthTP"],
            [2130, -3984, "WindtornRuins.RuinsTP"],
            [422, -3864, "WillowsEnd.InnerTP"]
        ]
        icons_paths: dict[str, str] = {}
        shops: list[str] = ["TwillenShop.Overcharge",
                            "TwillenShop.TripleJump",
                            "TwillenShop.Wingclip",
                            "TwillenShop.Swap",
                            "TwillenShop.LightHarvest",
                            "TwillenShop.Vitality",
                            "TwillenShop.Energy",
                            "TwillenShop.Finesse",
                            "OpherShop.WaterBreath",
                            "OpherShop.Spike",
                            "OpherShop.SpiritSmash",
                            "OpherShop.Teleport",
                            "OpherShop.SpiritStar",
                            "OpherShop.Blaze",
                            "OpherShop.Sentry",
                            "OpherShop.ExplodingSpike",
                            "OpherShop.ShockSmash",
                            "OpherShop.StaticStar",
                            "OpherShop.ChargeBlaze",
                            "OpherShop.RapidSentry",
                            "LupoShop.HCMapIcon",
                            "LupoShop.ECMapIcon",
                            "LupoShop.ShardMapIcon"
                            ]
        for loc in shops:
            item = world.get_location(loc, player).item
            icon_path = get_item_iconpath(self, item, bool(options.shop_keywords))
            icons_paths.update({loc: icon_path})

        slot_data: dict[str, Any] = {
            "difficulty": logic_difficulty[options.difficulty.value],
            "glitches": bool(options.glitches.value),
            "spawn_x": coord[options.spawn.value][0],
            "spawn_y": coord[options.spawn.value][1],
            "spawn_anchor": coord[options.spawn.value][2],
            "goal_trees": bool("trees" in options.goal),
            "goal_quests": bool("quests" in options.goal),
            "goal_wisps": bool("wisps" in options.goal),
            "hard": bool(options.hard_mode.value),
            "qol": bool(options.qol.value),
            "hints": bool(options.hints.value),
            "knowledge_hints": bool(options.knowledge_hints.value),
            "better_spawn": bool(options.better_spawn.value),
            "better_wellspring": bool(options.better_wellspring.value),
            "no_rain": bool(options.no_rain.value),
            "skip_boss": bool("Everything" in options.no_combat or "Bosses" in options.no_combat),
            "skip_demi_boss": bool("Everything" in options.no_combat or "Demi Bosses" in options.no_combat),
            "skip_shrine": bool("Everything" in options.no_combat or "Shrines" in options.no_combat),
            "skip_arena": bool("Everything" in options.no_combat or "Arenas" in options.no_combat),
            "no_trials": bool(options.no_trials.value),
            "no_hearts": bool(options.no_hearts.value),
            "no_hand_quest": bool(options.quests == Quests.option_no_hand or options.quests == Quests.option_none),
            "no_quests": bool(options.quests == Quests.option_none),
            "no_ks": bool(options.no_ks.value),
            "open_mode": bool(options.open_mode),
            "glades_done": bool(options.glades_done),
            "shop_icons": icons_paths,
            "bonus": bool(options.extra_bonus or options.skill_upgrade)
        }

        return slot_data


class WotWItem(Item):
    game: str = "Ori and the Will of the Wisps"


class WotWLocation(Location):
    game: str = "Ori and the Will of the Wisps"
