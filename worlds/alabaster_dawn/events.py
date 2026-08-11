from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import ADWorld

from rule_builder.rules import Has, HasAll, HasAny, OptionFilter
from .options import DivineArtLogic

da_filter = [OptionFilter(DivineArtLogic, True)]

has_blunt = Has("Hammer") | da_filter & (
        HasAll("Ring of Rocks", "Physis")
        | HasAll("Boom Snare", "Aether")
)
# Blunt range not needed now since bombs don't exist yet
has_pierce = Has("Crossbow") | da_filter & (
        HasAll("Bramble Quake", "Physis")
        | HasAll("Cragspike Salvo", "Physis")
        | HasAll("Bolt Barrage", "Aether")
)
has_pierce_range = Has("Crossbow") | da_filter & (
        HasAll("Cragspike Salvo", "Physis")
        | HasAll("Bolt Barrage", "Aether")
)
has_slash = HasAny("Sword", "Chakram") | da_filter & (
        HasAll("Verdant Saw", "Physis")
        | HasAll("Leaf Blades", "Physis")
        | HasAll("Zapflash Slash", "Aether")
        | HasAll("Crack Shock", "Aether")
)
has_slash_range = Has("Chakram") | da_filter & (
        HasAll("Leaf Blades", "Physis")
        | HasAll("Crack Shock", "Aether")
)

has_range = HasAny("Crossbow", "Chakram", "Kama")
has_melee = HasAny("Sword", "Hammer")
has_combat = has_range | has_melee

def create_events(world: ADWorld):
    world.create_event("Blunt", has_blunt, "Menu")
    world.create_event("Pierce", has_pierce, "Menu")
    world.create_event("Pierce Range", has_pierce_range, "Menu")
    world.create_event("Slash", has_slash, "Menu")
    world.create_event("Slash Range", has_slash_range, "Menu")
    world.create_event("Range", has_range, "Menu")
    world.create_event("Melee", has_melee, "Menu")
    world.create_event("Combat", has_combat, "Menu")
