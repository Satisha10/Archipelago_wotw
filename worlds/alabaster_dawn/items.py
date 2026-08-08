from BaseClasses import ItemClassification as IC

from .data_structures import ItemData

# TODO Community levels: use the first level for regrowth / cleanse nest ?

items: dict[str, ItemData] = {
    "Physis": ItemData(
        classification=IC.progression | IC.useful,
        id=1,
        item_type="Element",
    ),
    "Aether": ItemData(
        classification=IC.progression | IC.useful,
        id=2,
        item_type="Element",
    ),
    "Sword": ItemData(
        classification=IC.progression | IC.useful,
        id=11,
        item_type="Melee weapon",
    ),
    "Hammer": ItemData(
        classification=IC.progression | IC.useful,
        id=12,
        item_type="Melee weapon",
    ),
    "Crossbow": ItemData(
        classification=IC.progression | IC.useful,
        id=21,
        item_type="Range weapon",
    ),
    "Chakram": ItemData(
        classification=IC.progression | IC.useful,
        id=22,
        item_type="Range weapon",
    ),
    "Kama": ItemData(
        classification=IC.progression | IC.useful,
        id=23,
        item_type="Range weapon",
    ),
    "Filia": ItemData(
        classification=IC.progression | IC.useful,
        id=30,
        item_type="Party member",
    ),
    "Lyhamn level": ItemData(
        classification=IC.progression | IC.useful,
        id=40,
        item_type="Community level",
    ),
    "Valley bridges repaired": ItemData(
        classification=IC.progression,
        id=60,
        item_type="Area access",
    ),
    "Low tide": ItemData(
        classification=IC.progression,
        id=61,
        item_type="Area access",
    ),
    "Boat travel": ItemData(
        classification=IC.progression,
        id=62,
        item_type="Area access",
    ),
    "Fulcrum Mark": ItemData(
        classification=IC.progression,
        id=80,
        pool_quantity=2,
        game_name="the-key",
        item_type="Key",
    ),
    "Trial Mark": ItemData(
        classification=IC.progression,
        id=81,
        pool_quantity=2,
        game_name="the-key-dng",
        item_type="Key",
    ),
    "Whisper of the gods x5": ItemData(
        classification=IC.progression,
        id=101,
        item_quantity=5,
        game_name="chest-ess-1-whisper",
        item_type="Craft (limited)",
    ),
    "Verse of the Gods x3": ItemData(
        classification=IC.progression,
        id=102,
        item_quantity=3,
        game_name="chest-ess-2-verse",
        item_type="Craft (limited)",
    ),

    # TODO loot items (fillers)
    # TODO gems, constructs
    # TODO dish recipies
    # TODO Artefacts
}
