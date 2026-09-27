"""Major gems. Item ID band: 600-899"""

from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

major_gems: dict[str, ItemData] = {
    "Chipped Edge": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mel-str-01",
        item_type="Gem",
        item_id=600,
    ),
    "Bent Edge": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mel-crit-01",
        item_type="Gem",
        item_id=605,
    ),
    "Ruff Edge": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mel-spec-01",
        item_type="Gem",
        item_id=610,
    ),
    "Shaggy Quill": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="rng-str-01",
        item_type="Gem",
        item_id=615,
    ),
    "Fickle Quill": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="rng-crit-01",
        item_type="Gem",
        item_id=620,
    ),
    "Dirty Quill": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="rng-spec-01",
        item_type="Gem",
        item_id=625,
    ),
    "Dim Halo": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-l-def-01",
        item_type="Gem",
        item_id=630,
    ),
    "Vexed Halo": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-l-off-01",
        item_type="Gem",
        item_id=635,
    ),
    "Spirit Laurel": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-r-def-01",
        item_type="Gem",
        item_id=640,
    ),
    "Crude Laurel": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="up-maj-r-off-01",
        item_type="Gem",
        item_id=645,
    ),
    "Flexing Bracer": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-l-off-01",
        item_type="Gem",
        item_id=650,
    ),
    "Stiff Bracer": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-l-def-01",
        item_type="Gem",
        item_id=655,
    ),
    "Ruffian's Gauntlet": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-r-off-01",
        item_type="Gem",
        item_id=660,
    ),
    "Plebian Gauntlet": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="mid-maj-r-def-01",
        item_type="Gem",
        item_id=665,
    ),
    "Brittle Shell": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-l-def-01",
        item_type="Gem",
        item_id=670,
    ),
    "Light Shell": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-l-off-01",
        item_type="Gem",
        item_id=675,
    ),
    "Simple Cuirass": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-r-def-01",
        item_type="Gem",
        item_id=680,
    ),
    "Runner's Cuirass": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="low-maj-r-off-01",
        item_type="Gem",
        item_id=685,
    ),
}
