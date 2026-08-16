"""Locations for main unlocks in the game (elements, weaving nests and spires)."""
from rule_builder.rules import Has, HasAll, True_

from .rule_helpers import has_any_elements
from .data_structures import StoryLocData

story_loc: dict[str, StoryLocData] = {
    "Aether.Element": StoryLocData(
        game_name="TODO",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce") & Has("Trial Mark", count=2)  # TODO check
    ),
    "Valley.TODO.Nest": StoryLocData(
        game_name="Valley Nest",
        area="Koro Valley",
        rule=Has("Range"),
    ),
    "Plains.TODO.Nest": StoryLocData(
        game_name="Plains Nest",
        area="Aurum Plains",
        rule=HasAll("Combat", "Slash", "Blunt"),
    ),
    "EternalSpring.Nest": StoryLocData(
        game_name="Eternal Spring nest",
        area="Eternal Spring",
        rule=has_any_elements(2) & Has("Pierce Range"),
    ),
    "Aether.TODO.Spire": StoryLocData(
        game_name="Aether Spire",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Aether"),  # TODO Also finsh the dungeon
    ),
}
