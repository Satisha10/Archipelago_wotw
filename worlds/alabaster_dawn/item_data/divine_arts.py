from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

arts: dict[str, ItemData] = {
    "Bramble Quake": ItemData(  # Pierce
        classification=IC.useful,
        game_name="phy-mel-grass1",
        item_type="Divine Art",
    ),
    "Verdant Saw": ItemData(  # Slash
        classification=IC.useful,
        game_name="phy-mel-grass2",
        item_type="Divine Art",
    ),
    "Leaf Blades": ItemData(  # Slash
        classification=IC.useful,
        game_name="phy-rgd-status1",
        item_type="Divine Art",
    ),
    "Cragspike Salvo": ItemData(  # Pierce
        classification=IC.useful,
        game_name="phy-rgd-dps1",
        item_type="Divine Art",
    ),
    "Ring of Rocks": ItemData(  # Blunt
        classification=IC.useful,
        game_name="phy-grd-shield1",
        item_type="Divine Art",
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
    ),
    "Zapflash Slash": ItemData(  # Slash
        classification=IC.useful,
        game_name="aet-mel-dps1",
        item_type="Divine Art",
    ),
    "Crack Shock": ItemData(  # Slash
        classification=IC.useful,
        game_name="aet-rgd-status1",
        item_type="Divine Art",
    ),
    "Bolt Barrage": ItemData(  # Pierce
        classification=IC.useful,
        game_name="aet-rgd-beam1",
        item_type="Divine Art",
    ),
    "Stardrop Counter": ItemData(
        classification=IC.useful,
        game_name="aet-grd-evadeAtk",
        item_type="Divine Art",
    ),
}
