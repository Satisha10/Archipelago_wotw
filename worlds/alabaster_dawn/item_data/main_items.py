from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

items: dict[str, ItemData] = {
    "Test": ItemData(  # TODO Remove
        classification=IC.filler,
        item_type="Element",
        game_name="test",
        pool_quantity=0,
    ),
    "Physis": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Element",
        pool_quantity=0,
        game_name="ELEMENT:14",
    ),
    "Aether": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Element",
        game_name="ELEMENT:15",
    ),
    "Sword": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Melee weapon",
        pool_quantity=0,
        game_name="WEAPON:sword",
    ),
    "Hammer": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Melee weapon",
        game_name="WEAPON:hammer",
    ),
    "Crossbow": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Range weapon",
        pool_quantity=0,
        game_name="WEAPON:crossbow",
    ),
    "Chakram": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Range weapon",
        game_name="WEAPON:chakram",
    ),
    "Kama": ItemData(
        classification=IC.progression | IC.useful,
        item_type="Range weapon",
        game_name="WEAPON:kama",
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
    ),
    "Valley bridges repaired": ItemData(
        classification=IC.progression,
        item_type="Area access",
        game_name="PLOT:ap_bridges.received",
    ),
    "Low tide": ItemData(
        classification=IC.progression,
        item_type="Area access",
        game_name="PLOT:ap_tide.received",
    ),
    "Boat travel": ItemData(
        classification=IC.progression,
        item_type="Area access",
        game_name="PLOT:ap_boat.received",
    ),
    "Fulcrum Mark": ItemData(
        classification=IC.progression,
        pool_quantity=2,
        game_name="the-key",
        item_type="Key",
    ),
    "Trial Mark": ItemData(
        classification=IC.progression,
        pool_quantity=2,
        game_name="the-key-dng",
        item_type="Key",
    ),
    "Divine Connection": ItemData(
        classification=IC.useful,
        pool_quantity=1,
        game_name="Divine Connection",
        item_type="Upgrade",
    ),
}
