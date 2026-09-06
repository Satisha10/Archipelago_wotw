from .data_structures import QuestData

from rule_builder.rules import Has, HasAll

quests: dict[str, QuestData] = {
    "Branching Out": QuestData(
        area="Koro Valley",
        game_name="quickwood",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Range"),
    ),
    "Rice to the Occasion": QuestData(
        area="Koro Valley",
        game_name="ricefarm",
        level_progress="Lyhamn",
        rule=HasAll("Range", "Blunt"),
    ),
    "Blooming Villain": QuestData(
        area="Koro Valley",
        game_name="flowerBoss1",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Range"),
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
        rule=HasAll("Hammer", "Chakram")
    ),
    "Nuemera Island": QuestData(
        area="Aurum Plains",
        game_name="grandPass",
        level_progress="Sundalan",
        rule=HasAll("Kama", "Blunt", "Pierce", "Aether", "Slash")
    ),
    # Side quests
    "Quick Quickwood Query": QuestData(
        area="Koro Valley",
        game_name="southBarrier1",
        level_progress="Lyhamn",
        # Blunt required because Branching Out (quickwood) must be done beforehand
        rule=HasAll("Range", "Valley bridges", "Blunt"),
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
        rule=Has("Range") & Has("Lyhamn level", count=1),
    ),
    "For the Children, right ?": QuestData(
        area="Lyhamn",
        game_name="teacherStash",
        level_progress="Lyhamn",
        # Requires Rice to the Occasion to progress
        rule=HasAll("Blunt", "Range") & Has("Lyhamn level", count=1),
    ),
    "Spring's Return": QuestData(
        area="Lyhamn",
        game_name="bathHouse1",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Filia", "Chakram", "Aether"),
    ),
    "The Fervor of Youth": QuestData(
        area="Lyhamn",
        game_name="hotHeadLad1",
        level_progress=None,
        # Blunt required because Branching Out (quickwood) must be done beforehand
        rule=HasAll("Blunt", "Range") & Has("Lyhamn level", count=1)
    ),
    "Free the Fish": QuestData(
        area="Lyhamn",
        game_name="lakeFish1",
        level_progress="Lyhamn",
        # TODO combat logic, the boss seems to have a fixed level (16 here)
        rule=HasAll("Range", "Aether", "Blunt") & Has("Lyhamn level", count=1),
    ),
}
