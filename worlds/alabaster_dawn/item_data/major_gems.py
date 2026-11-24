"""Major gems. Item ID band: 600-899"""

from ..data_structures import GemData, GemSlot

major_gems: dict[str, GemData] = {
    "Chipped Edge": GemData(
        game_name="mel-str-01",
        item_id=600,
        slot=GemSlot.melee,
        purity=1,
    ),
    "Bent Edge": GemData(
        game_name="mel-crit-01",
        item_id=605,
        slot=GemSlot.melee,
        purity=1,
    ),
    "Humble Edge": GemData(
        game_name="mel-spec-01",
        item_id=610,
        slot=GemSlot.melee,
        purity=1,
    ),
    "Shaggy Quill": GemData(
        game_name="rng-str-01",
        item_id=615,
        slot=GemSlot.ranged,
        purity=1,
    ),
    "Fickle Quill": GemData(
        game_name="rng-crit-01",
        item_id=620,
        slot=GemSlot.ranged,
        purity=1,
    ),
    "Dirty Quill": GemData(
        game_name="rng-spec-01",
        item_id=625,
        slot=GemSlot.ranged,
        purity=1,
    ),
    "Dim Halo": GemData(
        game_name="up-maj-l-def-01",
        item_id=630,
        slot=GemSlot.ul,
        purity=1,
    ),
    "Vexed Halo": GemData(
        game_name="up-maj-l-off-01",
        item_id=635,
        slot=GemSlot.ul,
        purity=1,
    ),
    "Budding Halo": GemData(
        game_name="up-maj-l-mhp-01",
        item_id=690,
        slot=GemSlot.ul,
        purity=1,
    ),
    "Aged Laurel": GemData(
        game_name="up-maj-r-def-01",
        item_id=640,
        slot=GemSlot.ur,
        purity=1,
    ),
    "Crude Laurel": GemData(
        game_name="up-maj-r-off-01",
        item_id=645,
        slot=GemSlot.ur,
        purity=1,
    ),
    "Withering Laurel": GemData(
        game_name="up-maj-r-sts-01",
        item_id=695,
        slot=GemSlot.ur,
        purity=1,
    ),
    "Flexing Bracer": GemData(
        game_name="mid-maj-l-off-01",
        item_id=650,
        slot=GemSlot.ml,
        purity=1,
    ),
    "Stiff Bracer": GemData(
        game_name="mid-maj-l-def-01",
        item_id=655,
        slot=GemSlot.ml,
        purity=1,
    ),
    "Flinger's Bracer": GemData(
        game_name="mid-maj-l-ext-01",
        item_id=700,
        slot=GemSlot.ml,
        purity=1,
    ),
    "Ruffian's Gauntlet": GemData(
        game_name="mid-maj-r-off-01",
        item_id=660,
        slot=GemSlot.mr,
        purity=1,
    ),
    "Plebeian Gauntlet": GemData(
        game_name="mid-maj-r-def-01",
        item_id=665,
        slot=GemSlot.mr,
        purity=1,
    ),
    "Glimmering Gauntlet": GemData(
        game_name="mid-maj-r-ext-01",
        item_id=705,
        slot=GemSlot.mr,
        purity=1,
    ),
    "Brittle Shell": GemData(
        game_name="low-maj-l-def-01",
        item_id=670,
        slot=GemSlot.ll,
        purity=1,
    ),
    "Light Shell": GemData(
        game_name="low-maj-l-off-01",
        item_id=675,
        slot=GemSlot.ll,
        purity=1,
    ),
    "Dubious Shell": GemData(
        game_name="low-maj-l-art-01",
        item_id=710,
        slot=GemSlot.ll,
        purity=1,
    ),
    "Simple Cuirass": GemData(
        game_name="low-maj-r-def-01",
        item_id=680,
        slot=GemSlot.lr,
        purity=1,
    ),
    "Runner's Cuirass": GemData(
        game_name="low-maj-r-off-01",
        item_id=685,
        slot=GemSlot.lr,
        purity=1,
    ),
    "Painted Cuirass": GemData(
        game_name="low-maj-r-yum-01",
        item_id=715,
        slot=GemSlot.lr,
        purity=1,
    ),
}
