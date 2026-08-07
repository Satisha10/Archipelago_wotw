from __future__ import annotations

from typing import Any

from worlds.AutoWorld import World, WebWorld

from BaseClasses import Item, Location, Region, Tutorial

from .options import ADOptions, option_groups
from .areas import areas
from .items import items
from .chests import chests
from .quests import quests
from .locations import location_name_to_id

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

    origin_region_name = "Lyhamn"

    def create_regions(self) -> None:
        mworld = self.multiworld
        player = self.player
        for name in areas:  # Create the regions
            region = Region(name, player, mworld)
            mworld.regions.append(region)

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

        # TODO options, separate main quests ?
        for quest, quest_data in quests.items():
            region = self.get_region(quest_data.area)
            quest_loc = ADLocation(self.player, quest, location_name_to_id[quest], region)
            region.locations.append(quest_loc)
            self.set_rule(quest_loc, quest_data.rule)

        for dish, dish_data in quests.items():
            region = self.get_region("Lyhamn")
            dish_loc = ADLocation(self.player, dish, location_name_to_id[dish], region)
            region.locations.append(dish_loc)
            self.set_rule(dish_loc, dish_data.rule)

    def create_items(self) -> None:
        for name in items.keys():
            self.create_item(name)

    def create_item(self, name: str) -> ADItem:
        return ADItem(name, items[name].classification, items[name].id, self.player)

    def get_filler_item_name(self) -> str:  # TODO
        return "TODO"

    def fill_slot_data(self) -> dict[str, Any]:
        return self.options.as_dict(
            "quests",
            "craftsanity",
            "cooksanity",
        )

class ADItem(Item):
    game: str = "Alabaster Dawn"

class ADLocation(Location):
    game: str = "Alabaster Dawn"
