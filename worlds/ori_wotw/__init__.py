"""AP world for Ori and the Will of the Wisps."""

# TODO Relics ? Black market ?
# TODO fix the in-game location counter
# TODO rename MultiWorld to mw and use new world API for regions
# TODO location groups (as a set)
# TODO Add relics to slot_data and client implementation
# TODO rename spawn locations and add aliases


from typing import Any
from collections import Counter

from entrance_rando import randomize_entrances
from .Rules import (set_moki_rules, set_gorlek_rules, set_gorlek_glitched_rules, set_kii_rules,
                    set_kii_glitched_rules, set_unsafe_rules, set_unsafe_glitched_rules)
from .AdditionalRules import combat_rules, unreachable_rules
from .Items import item_table
from .Items_Icons import get_item_iconpath
from .Locations import loc_table
from .Quests import quest_table
from .LocationGroups import loc_sets, location_regions
from .Events import event_table
from .Regions import region_table
from .Entrances import entrance_table
from .Refills import refill_events
from .Options import WotWOptions, option_groups, LogicDifficulty, Quests, StartingLocation
from .SpawnItems import spawn_items, spawn_names, early_items
from .Presets import options_presets
from .ItemGroups import item_groups
from .RulesFunctions import get_max, get_refill, get_enemy_cost, IMPOSSIBLE_COST
from .DoorData import doors_map, doors_vanilla

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
    The sequel to Ori and the blind forest, a platform game emphasizing exploration, collecting items and upgrades, and
    backtracking to previously inaccessible areas.
    The player controls the titular Ori, a white guardian spirit.
    """
    game = "Ori and the Will of the Wisps"
    web = WotWWeb()

    item_name_to_id = {name: data[2] for name, data in item_table.items()}
    location_name_to_id = loc_table

    item_name_groups = item_groups

    options_dataclass = WotWOptions
    options: WotWOptions

    required_client_version = (0, 5, 0)

    def __init__(self, multiworld, player) -> None:
        super(WotWWorld, self).__init__(multiworld, player)
        self.relic_areas: list[str] = []  # Store which areas contain a relic
        self.empty_locations: list[str] = []  # Excluded locations, for now hold a Nothing item

    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)
        # Ask to update the max resources and the refills on the next call to `RulesFunctions.has_enough_resources`
        if change and item.name in ("Health Fragment",
                                    "Energy Fragment",
                                    "EastHollow.ForestsVoice",
                                    "LowerReach.ForestsMemory",
                                    "UpperDepths.ForestsEyes",
                                    "WestPools.ForestsStrength",
                                    "WindtornRuins.Seir",):
            state.wotw_resource_stale[self.player] = True
        # Ask to update the combat data on the next call to `RulesFunctions.compute_combat`
        elif change and item.name in ("Hammer",
                                      "Sword",
                                      "Grenade",
                                      "Bow",
                                      "Shuriken",
                                      "Sentry",
                                      "Spear",
                                      "Blaze",
                                      "Flash",
                                      "Combat.Ranged",
                                      "Combat.Aerial",
                                      "Combat.Dangerous",
                                      "Combat.Shielded",
                                      "Combat.Bat",
                                      "Combat.Sand",
                                      ):
            state.wotw_enemies_stale_collect[self.player] = True
        return change

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        # Ask to update the max resources and the refills on the next call to `RulesFunctions.has_enough_resources`
        if change and item.name in ("Health Fragment",
                                    "Energy Fragment",
                                    "EastHollow.ForestsVoice",
                                    "LowerReach.ForestsMemory",
                                    "UpperDepths.ForestsEyes",
                                    "WestPools.ForestsStrength",
                                    "WindtornRuins.Seir",):
            state.wotw_resource_stale[self.player] = True
        # Ask to update the combat data on the next call to `RulesFunctions.compute_combat`
        elif change and item.name in ("Hammer",
                                      "Sword",
                                      "Grenade",
                                      "Bow",
                                      "Shuriken",
                                      "Sentry",
                                      "Spear",
                                      "Blaze",
                                      "Flash",
                                      "Combat.Ranged",
                                      "Combat.Aerial",
                                      "Combat.Dangerous",
                                      "Combat.Shielded",
                                      "Combat.Bat",
                                      "Combat.Sand",
                                      ):
            state.wotw_enemies_stale_remove[self.player] = True
        return change

    def generate_early(self) -> None:
        options = self.options
        # Options checking
        if options.open_mode:
            options.no_rain.value = True
        # Escaping from Willow require to complete the elevator fight, so a tp is needed to escape.
        if options.spawn.value == StartingLocation.option_willow and not options.tp:
            options.spawn.value = StartingLocation.option_marsh  # No TP in pool: spawn somewhere else.
        # Without TP in the pool, some random spawn are dead-ends without better random spawn
        if not options.tp and not options.better_spawn:
            options.better_spawn.value = True

        # Selection of a random goal
        if "random" in options.goal:
            possible_goals = list(options.goal.value)
            possible_goals.remove("random")
            selected_goal: list = []
            if not possible_goals:  # Only random selected, choose among all goals
                possible_goals = ["trees", "wisps", "quests", "relics"]
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
        mworld = self.multiworld
        player = self.player
        options = self.options

        for region_name in region_table:
            region = Region(region_name, player, mworld)
            mworld.regions.append(region)

        for region_name in doors_map.keys():
            region = Region(region_name, player, mworld)
            mworld.regions.append(region)

        menu_region = Region("Menu", player, mworld)
        mworld.regions.append(menu_region)

        spawn_name = spawn_names[options.spawn]
        spawn_region = self.get_region(spawn_name)  # Links menu with spawn point
        menu_region.connect(spawn_region, rule=lambda state: True)

        menu_region.connect(self.get_region("HeaderStates"), rule=lambda state: True)

        for loc_name in loc_table.keys():  # Create regions on locations
            region = Region(loc_name, player, mworld)
            mworld.regions.append(region)
            region.locations.append(WotWLocation(player, loc_name, self.location_name_to_id[loc_name], region))
        for quest_name in quest_table:  # Quests are locations that have to be tracked like events
            event_name = quest_name + ".quest"
            event_region = Region(event_name, player, mworld)  # Region that holds the event item
            mworld.regions.append(event_region)
            event_loc = WotWLocation(player, event_name, None, event_region)
            event_loc.show_in_spoiler = False
            event_loc.place_locked_item(self.create_event_item(quest_name))
            event_region.locations.append(event_loc)
            base_region = self.get_region(quest_name)  # Region that holds the location
            base_region.connect(event_region, rule=lambda state: True)  # Connect the event region to the base region

        for event in event_table:  # Various events
            self.create_event(event)
        for event in refill_events:  # Tracks the refills that are accessible
            self.create_event(event)

        for entrance_name in entrance_table:  # Create and connect the entrances
            (parent, connected) = entrance_name.split(" -> ")
            parent_region = self.get_region(parent)
            connected_region = self.get_region(connected)
            entrance = parent_region.create_exit(entrance_name)
            entrance.access_rule = lambda state: False  # The rules are mostly set with add_rule, so start with False.
            entrance.connect(connected_region)

        self.create_event("Victory", show_spoiler=True)

        mworld.completion_condition[player] = lambda state: state.has("Victory", player)

    def create_event(self, event: str, show_spoiler=False) -> None:
        """Create an event, place the item and attach it to an event region (all with the same name)."""
        event_region = Region(event, self.player, self.multiworld)
        event_location = WotWLocation(self.player, event, None, event_region)
        event_location.show_in_spoiler = show_spoiler
        event_location.place_locked_item(self.create_event_item(event))
        self.multiworld.regions.append(event_region)
        event_region.locations.append(event_location)

    def create_item(self, name: str) -> "WotWItem":
        return WotWItem(name, item_table[name][1], item_table[name][2], player=self.player)

    def create_items(self) -> None:
        mworld = self.multiworld
        options = self.options

        skipped_items: list[str] = []  # Remove one instance of the item
        removed_items: list[str] = []  # Remove all instances of the item

        # TODO Check if random must be taken from mw or world
        for item in spawn_items(self, options.spawn.value, options.difficulty.value):  # Staring items
            mworld.push_precollected(self.create_item(item))
            skipped_items.append(item)

        for item, count in options.start_inventory.value.items():
            for _ in range(count):
                skipped_items.append(item)

        if options.sword:
            mworld.push_precollected(self.create_item("Sword"))
            removed_items.append("Sword")

        if not options.tp:
            for item in item_groups["Teleporters"]:
                removed_items.append(item)

        if not options.extratp:
            for item in item_groups["Extra Teleporters"]:
                removed_items.append(item)

        if not options.bonus:
            for item in item_groups["Bonus"]:
                removed_items.append(item)

        if not options.extra_bonus:
            for item in item_groups["Bonus+"]:
                removed_items.append(item)

        if not options.skill_upgrade:
            for item in item_groups["Skill Upgrades"]:
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
                loc = self.get_location(location)
                loc.place_locked_item(self.create_item(item))
                removed_items.append(item)

        if options.launch_on_seir:
            self.get_location("WindtornRuins.Seir").place_locked_item(self.create_item("Launch"))
            removed_items.append("Launch")

        for location in self.empty_locations:  # TODO temporary workaround
            loc = self.get_location(location)
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

        if options.difficulty == LogicDifficulty.option_moki:
            # Exclude a location that is inaccessible in the lowest difficulty.
            skipped_loc = self.get_location("WestPools.BurrowOre")
            skipped_loc.progress_type = LocationProgressType.EXCLUDED

        # TODO Add relics to Items.py, and add for each area ? (or do that client side)
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
                while relic_location in self.empty_locations:  # Reroll if the location is excluded
                    relic_location = self.random.choice(location_regions[area])
                self.get_location(relic_location).place_locked_item(self.create_item("Relic"))

        # Add some items to sphere 1
        items, ks_amount = early_items(self, options.spawn.value)
        for item in items:
            self.multiworld.early_items[self.player][item] = 1
        if not options.no_ks and ks_amount > 0:
            self.multiworld.early_items[self.player]["Keystone"] = ks_amount

        # Add filler items to have the same number of items and locations
        extras = len(mworld.get_unfilled_locations(player=self.player)) - len(pool)
        pool += [self.create_item(self.get_filler_item_name()) for _ in range(extras)]

        mworld.itempool += pool

    def create_event_item(self, event: str) -> "WotWItem":
        return WotWItem(event, ItemClassification.progression, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(["50 Spirit Light", "100 Spirit Light"])

    def connect_to_menu(self, region: str) -> None:
        """Connect the region to menu (if the connection does not already exist)."""
        if not self.multiworld.regions.entrance_cache[self.player].get(f"Menu -> {region}"):
            self.get_region("Menu").connect(self.get_region(region))

    def set_rules(self) -> None:
        player = self.player
        options = self.options
        difficulty = options.difficulty

        # Add the basic rules.
        set_moki_rules(self)
        combat_rules(self)
        unreachable_rules(self)

        # Add rules depending on the logic difficulty.
        if difficulty == LogicDifficulty.option_moki:
            # Extra rule for a location that is inaccessible in the lowest difficulty.
            add_rule(self.get_entrance("WestPools.Teleporter -> WestPools.BurrowOre"),
                     lambda state: state.has_all(("Burrow", "Clean Water", "Water Dash"), player), "or")
        if difficulty >= LogicDifficulty.option_gorlek:
            set_gorlek_rules(self)
            if options.glitches:
                set_gorlek_glitched_rules(self)
        if difficulty >= LogicDifficulty.option_kii:
            set_kii_rules(self)
            if options.glitches:
                set_kii_glitched_rules(self)
        if difficulty == LogicDifficulty.option_unsafe:
            set_unsafe_rules(self)
            if options.glitches:
                set_unsafe_glitched_rules(self)

        # Add victory condition
        victory_conn = self.get_region("WillowsEnd.ShriekArena").connect(self.get_region("Victory"))
        set_rule(victory_conn, lambda s: s.has_any(("Sword", "Hammer"), player)
                         and s.has_all(("Double Jump", "Dash", "Bash", "Grapple", "Glide", "Burrow", "Launch"), player))
        if "trees" in options.goal:
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
                         ]:
                add_rule(victory_conn, lambda s: s.can_reach_region(tree, player))
                # The entrance checks for regions, so we need to add an indirect condition
                self.multiworld.register_indirect_condition(self.get_region(tree), victory_conn)

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
            add_rule(victory_conn, lambda s: s.count("Relic", player) >= options.relic_count.value)

        # Rules for specific options
        if options.qol:
            self.connect_to_menu("GladesTown.TuleySpawned")
            self.get_region("WoodsEntry.LastTreeBranch").connect(self.get_region("WoodsEntry.TreeSeed"))
        if options.better_spawn:
            self.connect_to_menu("MarshSpawn.HowlBurnt")
            self.connect_to_menu("HowlsDen.BoneBarrier")
            self.connect_to_menu("EastPools.EntryLever")
            self.connect_to_menu("UpperWastes.LeverDoor")

        if "Everything" in options.no_combat or "Bosses" in options.no_combat:
            for entrance in ("HeaderStates -> SkipKwolok",
                             "HeaderStates -> SkipMora1",
                             "HeaderStates -> SkipMora2"):
                set_rule(self.get_entrance(entrance), lambda s: True)
        else:  # Connect these events when the seed is completed, to make them reachable.
            set_rule(self.get_entrance("HeaderStates -> SkipKwolok"),
                     lambda s: s.has("Victory", player))
            set_rule(self.get_entrance("HeaderStates -> SkipMora1"),
                     lambda s: s.has("Victory", player))
            set_rule(self.get_entrance("HeaderStates -> SkipMora2"),
                     lambda s: s.has("Victory", player))
        if "Everything" in options.no_combat or "Shrines" in options.no_combat:
            for entrance in (
                        "DenShrine -> HowlsDen.CombatShrineCompleted",
                        "MarshShrine -> MarshPastOpher.CombatShrineCompleted",
                        "GladesShrine -> WestGlades.CombatShrineCompleted",
                        "WoodsShrine -> WoodsMain.CombatShrineCompleted",
                        "DepthsShrine -> LowerDepths.CombatShrineCompleted"):
                set_rule(self.get_entrance(entrance), lambda s: True)

        if options.better_wellspring:
            self.connect_to_menu("InnerWellspring.TopDoorOpen")
        if options.no_ks:
            for event in ("MarshSpawn.KeystoneDoor",
                          "HowlsDen.KeystoneDoor",
                          "MarshPastOpher.EyestoneDoor",
                          "MidnightBurrows.KeystoneDoor",
                          "WoodsEntry.KeystoneDoor",
                          "WoodsMain.KeystoneDoor",
                          "LowerReach.KeystoneDoor",
                          "UpperReach.KeystoneDoor",
                          "UpperDepths.EntryKeystoneDoor",
                          "UpperDepths.CentralKeystoneDoor",
                          "UpperPools.KeystoneDoor",
                          "UpperWastes.KeystoneDoor"):
                self.connect_to_menu(event)
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
                self.connect_to_menu(event)
        if options.no_rain:
            for event in ("HowlsDen.UpperLoopExitBarrier",
                          "HowlsDen.UpperLoopEntranceBarrier",
                          "HowlsDen.RainLifted",):
                self.connect_to_menu(event)
            if not options.better_spawn:
                self.connect_to_menu("MarshSpawn.HowlBurnt")
        if options.glades_done:
            for event in ("TuleyShop.LastTreeBranchRejected",
                          "TuleyShop.SelaFlowers",
                          "TuleyShop.StickyGrass",
                          "TuleyShop.Lightcatchers",
                          "TuleyShop.BlueMoon",
                          "TuleyShop.SpringPlants",
                          "TuleyShop.LastTree"):
                self.connect_to_menu(event)
            # This location is unaccessible without Ore, so it is manually collected in this case
            self.connect_to_menu("GladesTown.RegrowTheGlades")
            for event in ("GladesTown.BuildHuts",
                          "GladesTown.RoofsOverHeads",
                          "GladesTown.OnwardsAndUpwards",
                          "GladesTown.ClearThorns",
                          "GladesTown.CaveEntrance"):
                self.connect_to_menu(event)

        if options.quests != Quests.option_none:  # Open locations locked behind NPCs
            # Connecting the other quests is not necessary, as their event don't appear in logic for non-quest locations
            for quest in ("WoodsEntry.LastTreeBranch",
                          "WoodsEntry.DollQI",
                          "GladesTown.FamilyReunionKey"):
                self.connect_to_menu(quest + ".quest")


    def connect_entrances(self) -> None:
        if self.options.door_rando:
            for door in doors_map:
                door_region: Region = self.get_region(door)
                door_region.create_exit(door)
                door_region.create_er_target(door)
            randomize_entrances(self, True, {0: [0]})
        else:
            for entry, target in doors_vanilla:
                self.get_region(entry).connect(self.get_region(target))


    def fill_slot_data(self) -> dict[str, Any]:
        # TODO Relics + ER
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
            item = self.get_location(loc).item
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
