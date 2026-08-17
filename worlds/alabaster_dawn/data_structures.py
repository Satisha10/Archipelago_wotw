"""Dataclasses for the items, locations and regions of the game."""

from __future__ import annotations

from dataclasses import dataclass

from BaseClasses import ItemClassification
from rule_builder.rules import Rule, True_


class ChestData:
    def __init__(self, area: str, game_name: str, rule: Rule = True_()):
        self.area = area
        self.game_name = game_name
        self.rule = rule


class StoryLocData:
    def __init__(self, area: str, game_name: str, rule: Rule = True_()):
        self.area = area
        self.game_name = game_name
        self.rule = rule


class DishData:
    def __init__(self, game_name: str, rule: Rule = True_()):
        self.game_name = game_name
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
    def __init__(self, area: str, game_name: str, level_progress: None | str = None, rule: Rule = True_()):
        self.area = area
        self.game_name = game_name
        self.level_progress = level_progress  # Progress for community level
        self.rule = rule


@dataclass
class ItemData:
    classification: ItemClassification
    pool_quantity: int = 1  # Base quantity for this item in the multiworld pool
    item_quantity: int = 1  # Quantity of the item received in-game each time
    game_name: str = ""
    item_type: str = ""
    id: int = 1  # Automatically set by the code generator

@dataclass
class APItem:
    id: int
    quantity: int
    classification: ItemClassification
