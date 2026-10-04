"""Locations for completing quests. Location ID Band: 1500-1999"""

from .data_structures import QuestData

from rule_builder.rules import Has, HasAll

quests: dict[str, QuestData] = {
    "Branching Out": QuestData(
        area="Koro Valley",
        game_name="quickwood",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Range"),
        loc_id=1500,
    ),
    "Rice to the Occasion": QuestData(
        area="Koro Valley",
        game_name="ricefarm",
        level_progress="Lyhamn",
        rule=HasAll("Range", "Blunt"),
        loc_id=1501,
    ),
    "Blooming Villain": QuestData(
        area="Koro Valley",
        game_name="flowerBoss1",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Range"),
        loc_id=1502,
    ),
    "A Sneak Peak": QuestData(
        area="Koro Valley",
        game_name="silverPeak",
        level_progress="Lyhamn",
        rule=HasAll("Chakram", "Blunt"),
        loc_id=1503,
    ),
    "Wheat Field Wack-A-mole": QuestData(
        area="Aurum Plains",
        game_name="oldFarm",
        level_progress="Sundalan",
        rule=HasAll("Hammer", "Chakram"),
        loc_id=1504,
    ),
    "Nuemera Island": QuestData(
        area="Aurum Plains",
        game_name="grandPass",
        level_progress="Sundalan",
        rule=HasAll("Kama", "Blunt", "Pierce", "Aether", "Slash"),
        loc_id=1505,
    ),
    # Side quests
    "Quick Quickwood Query": QuestData(
        area="Koro Valley",
        game_name="southBarrier1",
        level_progress="Lyhamn",
        # Blunt required because Branching Out (quickwood) must be done beforehand
        rule=HasAll("Blunt", "Range", "Valley bridges") & Has("Lyhamn level", count=1),
        loc_id=1506,
    ),
    "Temple Incursion": QuestData(
        area="Koro Valley",
        game_name="subDungeonMesa",
        level_progress=None,
        rule=HasAll("Blunt", "Filia", "Chakram") & Has("Fulcrum Mark", count=3),
        loc_id=1507,
    ),
    "Iron Deficiency": QuestData(
        area="Lyhamn",
        game_name="riverIron",
        level_progress="Lyhamn",
        rule=Has("Range") & Has("Lyhamn level", count=1),
        loc_id=1508,
    ),
    "For the Children, right ?": QuestData(
        area="Lyhamn",
        game_name="teacherStash",
        level_progress="Lyhamn",
        # Requires Rice to the Occasion to progress
        rule=HasAll("Blunt", "Range") & Has("Lyhamn level", count=1),
        loc_id=1509,
    ),
    "Spring's Return": QuestData(
        area="Lyhamn",
        game_name="bathHouse1",
        level_progress="Lyhamn",
        rule=HasAll("Blunt", "Filia", "Chakram", "Aether"),
        loc_id=1510,
    ),
    "The Fervor of Youth": QuestData(
        area="Lyhamn",
        game_name="hotHeadLad1",
        level_progress=None,
        # Blunt required because Branching Out (quickwood) must be done beforehand
        rule=HasAll("Blunt", "Range", "Valley bridges") & Has("Lyhamn level", count=1),
        loc_id=1511,
    ),
    "Free the Fish": QuestData(
        area="Lyhamn",
        game_name="lakeFish1",
        level_progress="Lyhamn",
        rule=HasAll("Range", "Aether", "Blunt") & Has("Lyhamn level", count=1),
        loc_id=1512,
    ),
}
