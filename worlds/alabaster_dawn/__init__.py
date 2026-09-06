from __future__ import annotations

from typing import Any

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, Location, Region, Tutorial, ItemClassification
from rule_builder.rules import Rule, True_, CanReachLocation
from .events import create_events

from .options import ADOptions, option_groups
from .areas import areas
from .items import items
from .chests import chests
from .quests import quests
from .dishes import dishes
from .story_locations import story_loc
from .locations import location_name_to_id
from .item_groups import item_groups

# TODO item groups

class ADWeb(WebWorld):
    theme = "ocean"  # TODO documentation
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setup the Alabaster Dawn randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Satisha"]
    )]
    option_groups = option_groups
    bug_report_page = "https://discord.com/channels/731205301247803413/1487693744177152030"

class ADWorld(World):
    """TODO, game description."""
    game = "Alabaster Dawn"

    options_dataclass = ADOptions
    options: ADOptions

    location_name_to_id = location_name_to_id
    item_name_to_id = {name: item.id for name, item in items.items()}

    item_name_groups = item_groups

    # Universal tracker support
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data
    ut_can_gen_without_yaml = True

    def generate_early(self) -> None:
        # Universal Tracker support
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            self.options.quests.value = slot_data["quests"]
            self.options.divine_logic.value = slot_data["divine_logic"]
            self.options.craftsanity.value = slot_data["craftsanity"]
            self.options.cooksanity.value = slot_data["cooksanity"]

    def create_regions(self) -> None:
        mworld = self.multiworld
        player = self.player
        menu_region = Region("Menu", player, mworld)
        mworld.regions.append(menu_region)
        for name in areas:  # Create the regions
            region = Region(name, player, mworld)
            mworld.regions.append(region)

        self.get_region("Menu").connect(self.get_region("Lyhamn"))  # TODO random spawn

        for base_name, area_data in areas.items():  # Connect the regions between them
            base_region = self.get_region(base_name)
            for target_name, rule in area_data.connections.items():
                target_region = self.get_region(target_name)
                self.create_entrance(base_region, target_region, rule)

        for chest, chest_data in chests.items():
            region = self.get_region(chest_data.area)
            chest_loc = ADLocation(self.player, chest, location_name_to_id[chest], region)
            region.locations.append(chest_loc)
            self.set_rule(chest_loc, chest_data.rule)

        for story, data in story_loc.items():
            region = self.get_region(data.area)
            story_location = ADLocation(self.player, story, location_name_to_id[story], region)
            region.locations.append(story_location)
            self.set_rule(story_location, data.rule)

        # TODO options, separate main quests ?
        for quest, quest_data in quests.items():
            region = self.get_region(quest_data.area)
            quest_loc = ADLocation(self.player, quest, location_name_to_id[quest], region)
            region.locations.append(quest_loc)
            self.set_rule(quest_loc, quest_data.rule)

        if self.options.cooksanity:
            for dish, dish_data in dishes.items():
                region = self.get_region("Lyhamn")
                dish_loc = ADLocation(self.player, dish, location_name_to_id[dish], region)
                region.locations.append(dish_loc)
                self.set_rule(dish_loc, dish_data.rule)

    def create_items(self) -> None:
        # TODO change item classification depending on settings
        mworld = self.multiworld
        pool: list[ADItem] = []

        for name, data in items.items():
            for _ in range(data.quantity):
                item = self.create_item(name)
                pool.append(item)

        # Add filler items to have the same number of items and locations
        extras = len(mworld.get_unfilled_locations(player=self.player)) - len(pool)
        pool += [self.create_item(self.get_filler_item_name()) for _ in range(extras)]

        mworld.itempool += pool

    def create_item(self, name: str) -> ADItem:
        return ADItem(name, items[name].classification, items[name].id, self.player)

    def get_filler_item_name(self) -> str:  # TODO use a random filler once they are implemented
        return self.random.choice(item_groups["Filler"])

    def create_event_item(self, event: str) -> ADItem:
        return ADItem(event, ItemClassification.progression, None, self.player)

    def create_event(self, event: str, rule: Rule = True_(), region: None | str = None, show_spoiler=False) -> None:
        """
        Create an event location/item pair, and attach the location to a region.

        :param event: Event name.
        :param rule: Location rule for the event.
        :param region: If None, create a new region with the same name as the event to attach it. Else, attach the event
        to the given region.
        :param show_spoiler: Show the event in the spoiler.
        """
        if region is None:
            event_region = Region(event, self.player, self.multiworld)
            self.multiworld.regions.append(event_region)
        else:
            event_region = self.get_region(region)
        event_location = ADLocation(self.player, event, None, event_region)
        event_location.show_in_spoiler = show_spoiler
        event_location.place_locked_item(self.create_event_item(event))

        event_region.locations.append(event_location)
        self.set_rule(event_location, rule)

    def set_rules(self) -> None:
        create_events(self)

        self.set_completion_rule(CanReachLocation("EternalSpring.Outside"))

    def fill_slot_data(self) -> dict[str, Any]:
        return self.options.as_dict(
            "quests",
            "divine_logic",
            "craftsanity",
            "cooksanity",
        )

class ADItem(Item):
    game: str = "Alabaster Dawn"

class ADLocation(Location):
    game: str = "Alabaster Dawn"
