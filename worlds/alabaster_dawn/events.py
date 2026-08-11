from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import ADWorld

from rule_builder.rules import Has, HasAll, HasAny, OptionFilter
from .options import DivineSkillLogic

ds_filter = [OptionFilter(DivineSkillLogic, True)]

# TODO Range/combat blunt + pierce...
has_blunt = Has("Hammer") | ds_filter & (HasAll("DS1", "Aether") | HasAll("DS2", "Aether"))  # TODO

has_range = HasAny("Crossbow", "Chakram", "Kama")
has_melee = HasAny("Sword", "Hammer")
has_combat = has_range | has_melee

def create_events(world: ADWorld):
    world.create_event("Blunt", has_blunt, "Menu")
    world.create_event("Range", has_range, "Menu")
    world.create_event("Melee", has_melee, "Menu")
    world.create_event("Combat", has_combat, "Menu")
