from .data_structures import QuestData

from rule_builder.rules import Has, HasAll

quests: dict[str, QuestData] = {
    "TODO0": QuestData(
        area="Koro Valley",
        game_name="quickwood",
        level_progress="Lyhamn",
        rule=Has("Hammer")
    ),
    "TODO1": QuestData(
        area="Koro Valley",
        game_name="ricefarm",
        level_progress="Lyhamn",
    ),
    "TODO2": QuestData(
        area="Koro Valley",
        game_name="flowerBoss1",
        level_progress="Lyhamn",
    ),
    "TODO3": QuestData(
        area="Koro Valley",
        game_name="silverPeak",
        level_progress="Lyhamn",
        rule=Has("Chakram")
    ),
    "TODO4": QuestData(
        area="Aurum Plains",
        game_name="oldFarm",
        level_progress="Sundalan",
        rule=Has("Hammer")
    ),
    "TODO5": QuestData(
        area="Aurum Plains",
        game_name="grandPass",
        level_progress="Sundalan",
        rule=Has("Kama")
    ),
    # Side quests
    "TODO6": QuestData(
        area="Koro Valley",
        game_name="southBarrier1",
        level_progress="Lyhamn",
    ),
    "TODO7": QuestData(
        area="Koro Valley",
        game_name="subDungeonMesa",
        level_progress=None,
        rule=HasAll("Hammer", "Fulcrum Mark")
    ),
    "TODO8": QuestData(
        area="Lyhamn",
        game_name="riverIron",
        level_progress="Lyhamn",
    ),
    "TODO9": QuestData(
        area="Lyhamn",
        game_name="teacherStash",
        level_progress="Lyhamn",
    ),
    "TODO10": QuestData(
        area="Lyhamn",
        game_name="bathHouse1",
        level_progress="Lyhamn",
        rule=Has("Hammer")
    ),
    "TODO11": QuestData(
        area="Lyhamn",
        game_name="hotHeadLad1",
        level_progress=None,
    ),
    "TODO12": QuestData(
        area="Lyhamn",
        game_name="lakeFish1",
        level_progress="Lyhamn",
        rule=Has("Hammer"),
    ),
}
