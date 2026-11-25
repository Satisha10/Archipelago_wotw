"""Relics that can be toggled for various bonus. Item ID band: 4000-4099."""

from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

relic_items: dict[str, ItemData] = {
    "Treasure Radar": ItemData(
        classification=IC.useful,
        item_type="Relic",
        game_name="chest-detector",
        pool_quantity=0,
        item_id=4000,
    ),
    "Winged Boots": ItemData(
        classification=IC.useful,
        item_type="Relic",
        game_name="speed-run",
        item_id=4001,
    ),
    "Great Attractor": ItemData(
        classification=IC.useful,
        item_type="Relic",
        game_name="attractor",
        item_id=4002,
    ),
    "Utility Belt I": ItemData(
        classification=IC.useful,
        item_type="Relic",
        game_name="loadout-ext-1",
        item_id=4003,
    ),
    "Utility Belt II": ItemData(
        classification=IC.useful,
        item_type="Relic",
        game_name="loadout-ext-2",
        item_id=4004,
    ),
}
