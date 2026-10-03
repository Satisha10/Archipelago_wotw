"""Divine arts. Item ID band: 1500-1699"""

from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

arts: dict[str, ItemData] = {
    "Bramble Quake": ItemData(  # Pierce
        classification=IC.useful,
        game_name="phy-mel-grass1",
        item_type="Divine Art",
        item_id=1500,
    ),
    "Verdant Saw": ItemData(  # Slash
        classification=IC.useful,
        game_name="phy-mel-grass2",
        item_type="Divine Art",
        item_id=1501,
    ),
    "Leaf Blades": ItemData(  # Slash
        classification=IC.useful,
        game_name="phy-rgd-status1",
        item_type="Divine Art",
        item_id=1502,
    ),
    "Cragspike Salvo": ItemData(  # Pierce
        classification=IC.useful,
        game_name="phy-rgd-dps1",
        item_type="Divine Art",
        item_id=1503,
    ),
    "Ring of Rocks": ItemData(  # Blunt
        classification=IC.useful,
        game_name="phy-grd-shield1",
        item_type="Divine Art",
        item_id=1504,
    ),
    #"Granite Counterslap": ItemData(
    #    classification=IC.useful,
    #    game_name="phy-grd-counter1",
    #    item_type="Divine Art",
    #),
    "Boom Snare": ItemData(  # Blunt
        classification=IC.useful,
        game_name="aet-mel-aoe1",
        item_type="Divine Art",
        item_id=1550,
    ),
    "Zapflash Slash": ItemData(  # Slash
        classification=IC.useful,
        game_name="aet-mel-dps1",
        item_type="Divine Art",
        item_id=1551,
    ),
    "Crack Shock": ItemData(  # Slash
        classification=IC.useful,
        game_name="aet-rgd-status1",
        item_type="Divine Art",
        item_id=1552,
    ),
    "Bolt Barrage": ItemData(  # Pierce
        classification=IC.useful,
        game_name="aet-rgd-beam1",
        item_type="Divine Art",
        item_id=1553,
    ),
    "Stardrop Counter": ItemData(
        classification=IC.useful,
        game_name="aet-grd-evadeAtk",
        item_type="Divine Art",
        item_id=1554,
    ),
    "Frost Reaver": ItemData(  # Slash
        classification=IC.useful,
        game_name="cry-mel-aoe1",
        item_type="Divine Art",
        item_id=1600,
    ),
}
