"""Dataclasses for the items, locations and regions of the game."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum

from BaseClasses import ItemClassification
from rule_builder.rules import Rule, True_


class ChestData:
    def __init__(self, area: str, game_name: str, loc_id: int, rule: Rule = True_()):
        self.area = area
        self.game_name = game_name
        self.loc_id = loc_id
        self.rule = rule


class StoryLocData:
    def __init__(self, area: str, game_name: str, loc_id: int, rule: Rule = True_()):
        self.area = area
        self.game_name = game_name
        self.loc_id = loc_id
        self.rule = rule


class DishData:
    def __init__(self, game_name: str, loc_id: int, rule: Rule = True_()):
        self.game_name = game_name
        self.loc_id = loc_id
        self.rule = rule


@dataclass
class AreaData:
    connections: dict[str, Rule]
    # drops: list[str]


@dataclass
class CraftData:
    name: str
#    rule: Rule = True_()
    purity: int = 1

class QuestData:
    def __init__(self, area: str, game_name: str, loc_id: int, level_progress: None | str = None, rule: Rule = True_()):
        self.area = area
        self.game_name = game_name
        self.loc_id = loc_id
        self.level_progress = level_progress  # Progress for community level
        self.rule = rule


@dataclass
class ItemData:
    classification: ItemClassification = ItemClassification.filler
    item_id: int = 1
    pool_quantity: int = 1  # Base quantity for this item in the multiworld pool
    item_quantity: int = 1  # Quantity of the item received in-game each time
    game_name: str = ""
    item_type: str = ""


class GemSlot(IntEnum):
    melee = 0
    ranged = 1
    ul = 2
    ur = 3
    ml = 4
    mr = 5
    ll = 6
    lr = 7
    core = 8
    melee_m = 9
    ranged_m = 10


@dataclass
class GemData(ItemData):
    slot: GemSlot = GemSlot.melee  # Should always be overridden
    purity: int = 1  # Between 1 and 5
    bp_id: int | None = None
    bp_name: str | None = None  # game name of the blueprint/construct
    previous_gem: str | None = None  # Name of the gem from the previous purity (currently unused)
    forge_cost: tuple[str, ...] = ()  # Currently unused
    # Overrides the default from ItemData
    pool_quantity: int = 0
    classification: ItemClassification = ItemClassification.useful


@dataclass
class APItem:
    id: int
    quantity: int
    classification: ItemClassification
