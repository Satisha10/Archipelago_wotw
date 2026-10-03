"""Locations for main unlocks in the game (elements, weaving nests and spires). Location ID Band: 1-199"""

from rule_builder.rules import Has, HasAll, True_, HasAny

from .rule_helpers import has_any_elements
from .data_structures import StoryLocData

story_loc: dict[str, StoryLocData] = {
    "Aether.Element": StoryLocData(
        game_name="Aether",
        area="Trial of Aether A",
        rule=HasAll("Filia", "Blunt", "Range") & Has("Trial Mark", count=2),
        loc_id=1,
    ),
    "Valley.Hammer": StoryLocData(
        game_name="hammer",
        area="Koro Valley",
        loc_id=2,
    ),
    "Valley.Chakram": StoryLocData(
        game_name="chakram",
        area="Silver Peak",
        rule=HasAll("Blunt", "Range"),
        loc_id=3,
    ),
    "Plains.Kama": StoryLocData(
        game_name="kama",
        area="Aurum Plains",
        rule=HasAll("Blunt", "Aether", "Combat") & HasAny("Slash", "Kama"),
        loc_id=4,
    ),
    "Valley.WeaveNest": StoryLocData(
        game_name="ap_nest_valley.weaved",
        area="Koro Valley",
        rule=Has("Range"),
        loc_id=5,
    ),
    "Plains.WeaveNest": StoryLocData(
        game_name="ap_nest_plains.weaved",
        area="Aurum Plains",
        # Slash/blunt not strictly required, but used to interrupt the boss attacks
        rule=HasAll("Combat", "Slash", "Blunt"),
        loc_id=6,
    ),
    "EternalSpring.WeaveNest": StoryLocData(
        game_name="subDungeonMesa.nestCleared",
        area="Eternal Spring",
        # Most requirements are in the area rule
        rule=has_any_elements(2) & Has("Pierce Range"),
        loc_id=7,
    ),
    "Aether.WeaveSpire": StoryLocData(
        game_name="ap_spire_aether.weaved",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce Range", "Aether", "Physis")
             & Has("Trial Mark", count=2),
        loc_id=8,
    ),
    "ScalaMoor.Spear": StoryLocData(
        game_name="spear",
        area="Swamp.DeepBog",
        rule=HasAll("Physis", "Kama"),
        loc_id=9,
    ),
    "Cryo.Element": StoryLocData(
        game_name="cryo",
        area="Cryo.1Door",
        rule=HasAll("Kama", "Filia"),
        loc_id=10,
    ),
    "Cryo.Spire": StoryLocData(
        game_name="ap_spire_cryo.weaved",
        area="Cryo.E",
        rule=Has("Cryo Key", count=4) & Has("Cryo"), # TODO See base levels for bosses
        loc_id=11,
    ),
}
