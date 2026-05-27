from typing import NamedTuple

class SpawnItems(NamedTuple):
    moki_hf: int  # How many health fragments are required to meet the region requirements
    gorlek_hf: int
    kii_hf: int
    require_regen: bool  # Regenerate is only required in moki and gorlek (and if regenerate_requirements is enabled)
    early_ks: int  # How many keystones to put in the early items
    # items_amount: int  # How many items to spawn with

# TODO KS amount

spawn_data: dict[str, SpawnItems] = {
    "MarshSpawn": SpawnItems(0, 0, 0, False, 0),
    "HowlsDen": SpawnItems(0, 0, 0, False, 0),
    "MarshPastOpher": SpawnItems(0, 0, 0, False, 0),
    "MidnightBurrows": SpawnItems(0, 0, 0, False, 0),
    "WestHollow": SpawnItems(0, 0, 0, False, 0),
    "EastHollow": SpawnItems(0, 0, 0, False, 0),
    "GladesTown": SpawnItems(0, 0, 0, False, 0),
    "WestGlades": SpawnItems(1, 0, 0, False, 0),
    "OuterWellspring": SpawnItems(1, 0, 0, False, 0),
    "InnerWellspring": SpawnItems(1, 0, 0, False, 0),
    "WoodsEntry": SpawnItems(2, 0, 0, True, 0),
    "WoodsMain": SpawnItems(2, 0, 0, True, 0),
    "LowerReach": SpawnItems(3, 0, 0, True, 0),
    "UpperReach": SpawnItems(3, 0, 0, True, 0),
    "UpperDepths": SpawnItems(3, 1, 1, True, 0),
    "LowerDepths": SpawnItems(3, 1, 1, True, 0),
    "PoolsApproach": SpawnItems(1, 0, 0, True, 0),
    "EastPools": SpawnItems(1, 0, 0, True, 0),
    "UpperPools": SpawnItems(1, 0, 0, True, 0),
    "WestPools": SpawnItems(1, 0, 0, True, 0),
    "LowerWastes": SpawnItems(5, 1, 1, True, 0),
    "UpperWastes": SpawnItems(5, 1, 1, True, 0),
    "WeepingRidge": SpawnItems(7, 3, 3, True, 0),
    "WillowsEnd": SpawnItems(7, 3, 3, True, 0),
}
