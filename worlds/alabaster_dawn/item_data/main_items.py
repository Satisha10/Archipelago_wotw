"""Main items that are usually required to unlock new areas. Item ID band: 1-29: """

from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

main_items: dict[str, ItemData] = {
    "Test": ItemData(  # TODO Remove
        classification=IC.useful,
        item_type="Element",
        game_name="test",
        pool_quantity=0,
        item_id=456123156,
    ),
    "Test2": ItemData(  # TODO Remove
        classification=IC.useful,
        item_type="Element",
        game_name="test2",
        pool_quantity=0,
        item_id=456123157,
    ),
    "Physis": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Element",
        pool_quantity=0,
        game_name="ELEMENT:14",
        item_id=1,
    ),
    "Aether": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Element",
        game_name="ELEMENT:15",
        item_id=2,
    ),
    "Cryo": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Element",
        game_name="ELEMENT:17",
        item_id=4,
    ),
    "Sword": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Melee weapon",
        pool_quantity=0,
        game_name="WEAPON:sword",
        item_id=10,
    ),
    "Hammer": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Melee weapon",
        game_name="WEAPON:hammer",
        item_id=11,
    ),
    "Spear": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Melee weapon",
        game_name="WEAPON:spear",
        item_id=12,
    ),
    "Crossbow": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Range weapon",
        pool_quantity=0,
        game_name="WEAPON:crossbow",
        item_id=15,
    ),
    "Chakram": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Range weapon",
        game_name="WEAPON:chakram",
        item_id=16,
    ),
    "Kama": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Range weapon",
        game_name="WEAPON:kama",
        item_id=17,
    ),
    #"Filia": ItemData(
    #    classification=IC.progression | IC.useful,
    #    id=30,
    #    item_type="Party member",
    #    game_name="PARTY:filia",
    #),
    "Lyhamn level": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Community level",
        game_name="CL:lyhamn",
        item_id=30,
    ),
    "Valley bridges": ItemData(
        classification=IC.progression,
        item_type="Area access",
        game_name="PLOT:ap_bridges.received",
        item_id=40,
    ),
    "Low tide": ItemData(
        classification=IC.progression,
        item_type="Area access",
        game_name="PLOT:ap_tide.received",
        item_id=41,
    ),
    "Boat travel": ItemData(
        classification=IC.progression,
        item_type="Area access",
        game_name="PLOT:ap_boat.received",
        item_id=42,
    ),
    "Fulcrum Mark": ItemData(
        classification=IC.progression,
        pool_quantity=3,
        game_name="the-key",
        item_type="Key",
        item_id=100,
    ),
    "Trial Mark": ItemData(
        classification=IC.progression,
        pool_quantity=0,
        game_name="the-key-dng",
        item_type="Key",
        item_id=101,
    ),
    "Aether Trial Mark": ItemData(
        classification=IC.progression,
        pool_quantity=2,
        game_name="ap-key-aether",
        item_type="Key",
        item_id=102,
    ),
    "Cryo Trial Mark": ItemData(
        classification=IC.progression,
        pool_quantity=4,
        game_name="ap-key-cryo",
        item_type="Key",
        item_id=103,
    ),
    "Divine Connection": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="Divine Connection",
        item_type="Upgrade",
        item_id=150,
    ),
}
