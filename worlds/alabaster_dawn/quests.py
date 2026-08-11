from .data_structures import QuestData

from rule_builder.rules import Has, HasAll

quests: dict[str, QuestData] = {
    "Branching Out": QuestData(
        area="Koro Valley",
        game_name="quickwood",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Combat"),
    ),
    "Rice to the Occasion": QuestData(
        area="Koro Valley",
        game_name="ricefarm",
        level_progress="Lyhamn",
        rule=Has("Range"),
    ),
    "Blooming Villain": QuestData(
        area="Koro Valley",
        game_name="flowerBoss1",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Combat"),  # TODO Maybe not required if shortcut from rice field ?
        # Also maybe range required because of previous scripted fight
    ),
    "A Sneak Peak": QuestData(
        area="Koro Valley",
        game_name="silverPeak",
        level_progress="Lyhamn",
        rule=HasAll("Chakram", "Blunt"),
    ),
    "Wheat Field Wack-A-mole": QuestData(
        area="Aurum Plains",
        game_name="oldFarm",
        level_progress="Sundalan",
        rule=Has("Hammer")
    ),
    "Nuemera Island": QuestData(
        area="Aurum Plains",
        game_name="grandPass",
        level_progress="Sundalan",
        rule=HasAll("Kama", "Blunt", "Pierce", "Aether")
    ),
    # Side quests
    "Quick Quickwood Query": QuestData(
        area="Koro Valley",
        game_name="southBarrier1",
        level_progress="Lyhamn",
        rule=Has("Range"),
    ),
    "Temple Incursion": QuestData(
        area="Koro Valley",
        game_name="subDungeonMesa",
        level_progress=None,
        rule=HasAll("Blunt", "Filia", "Chakram") & Has("Fulcrum Mark", count=2),
    ),
    "Iron Deficiency": QuestData(
        area="Lyhamn",
        game_name="riverIron",
        level_progress="Lyhamn",
        rule=Has("Range"),
    ),
    "For the Children, right ?": QuestData(
        area="Lyhamn",
        game_name="teacherStash",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Range"),
    ),
    "Spring's Return": QuestData(
        area="Lyhamn",
        game_name="bathHouse1",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Filia", "Chakram"),
    ),
    "The Fervor of Youth": QuestData(
        area="Lyhamn",
        game_name="hotHeadLad1",
        level_progress=None,
        rule=Has("Combat")
    ),
    "Free the Fish": QuestData(
        area="Lyhamn",
        game_name="lakeFish1",
        level_progress="Lyhamn",
        rule=HasAll("Range", "Aether"),
    ),
}
