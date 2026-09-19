"""Locations for main unlocks in the game (elements, weaving nests and spires)."""
from rule_builder.rules import Has, HasAll, True_, HasAny

from .rule_helpers import has_any_elements
from .data_structures import StoryLocData

story_loc: dict[str, StoryLocData] = {
    "Aether.Element": StoryLocData(
        game_name="Aether",
        area="Trial of Aether A",
        rule=HasAll("Filia", "Blunt", "Range") & Has("Trial Mark", count=2)
    ),
    "Valley.Hammer": StoryLocData(
        game_name="hammer",
        area="Koro Valley",
    ),
    "Valley.Chakram": StoryLocData(
        game_name="chakram",
        area="Silver Peak",
        rule=HasAll("Blunt", "Range")
    ),
    "Plains.Kama": StoryLocData(
        game_name="kama",
        area="Aurum Plains",
        rule=HasAll("Blunt", "Aether", "Combat") & HasAny("Slash", "Kama")
    ),
    "Valley.WeaveNest": StoryLocData(
        game_name="ap_nest_valley.weaved",
        area="Koro Valley",
        rule=Has("Range"),
    ),
    "Plains.WeaveNest": StoryLocData(
        game_name="ap_nest_plains.weaved",
        area="Aurum Plains",
        # Slash/blunt not strictly required, but used to interrupt the boss attacks
        rule=HasAll("Combat", "Slash", "Blunt"),
    ),
    "EternalSpring.WeaveNest": StoryLocData(
        game_name="subDungeonMesa.nestCleared",
        area="Eternal Spring",
        # Most requirements are in the area rule
        rule=has_any_elements(2) & Has("Pierce Range"),
    ),
    "Aether.WeaveSpire": StoryLocData(
        game_name="ap_spire_aether.weaved",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce Range", "Aether", "Physis")
             & Has("Trial Mark", count=2),
    ),
}
