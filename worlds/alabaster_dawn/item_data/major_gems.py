from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

major_gems: dict[str, ItemData] = {
    "Chipped Edge": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mel-str-01",
        item_type="Gem",
    ),
    "Bent Edge": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mel-crit-01",
        item_type="Gem",
    ),
    "Ruff Edge": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mel-spec-01",
        item_type="Gem",
    ),
    "Shaggy Quill": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="rng-str-01",
        item_type="Gem",
    ),
    "Fickle Quill": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="rng-crit-01",
        item_type="Gem",
    ),
    "Dirty Quill": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="rng-spec-01",
        item_type="Gem",
    ),
    "Dim Halo": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-l-def-01",
        item_type="Gem",
    ),
    "Vexed Halo": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-l-off-01",
        item_type="Gem",
    ),
    "Spirit Laurel": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-r-def-01",
        item_type="Gem",
    ),
    "Crude Laurel": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-r-off-01",
        item_type="Gem",
    ),
    "Flexing Bracer": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-l-off-01",
        item_type="Gem",
    ),
    "Stiff Bracer": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-l-def-01",
        item_type="Gem",
    ),
    "Ruffian's Gauntlet": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-r-off-01",
        item_type="Gem",
    ),
    "Plebian Gauntlet": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-r-def-01",
        item_type="Gem",
    ),
    "Brittle Shell": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-l-def-01",
        item_type="Gem",
    ),
    "Light Shell": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-l-off-01",
        item_type="Gem",
    ),
    "Simple Cuirass": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-r-def-01",
        item_type="Gem",
    ),
    "Runner's Cuirass": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-r-off-01",
        item_type="Gem",
    ),
}
