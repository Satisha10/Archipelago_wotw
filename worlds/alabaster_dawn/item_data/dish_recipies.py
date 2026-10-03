"""Cooking dishes. ID band: 1700-1999"""

from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

dishes: dict[str, ItemData] = {
    "Basic Ration": ItemData(
        classification=IC.useful,
        game_name="ration-basic",
        item_type="Dish Recipie",
        pool_quantity=0,
        item_id=1700,
    ),
    "Ring Ration": ItemData(
        classification=IC.useful,
        game_name="ration-ring",
        item_type="Dish Recipie",
        item_id=1701,
    ),
    "Scrambled Egg": ItemData(
        classification=IC.useful,
        game_name="scrambled-egg",
        item_type="Dish Recipie",
        item_id=1702,
    ),
    "Fried Rice": ItemData(
        classification=IC.useful,
        game_name="wild-rice-fried",
        item_type="Dish Recipie",
        pool_quantity=0,
        item_id=1703,
    ),
    "Ring Rolls": ItemData(
        classification=IC.useful,
        game_name="ring-rolls",
        item_type="Dish Recipie",
        item_id=1704,
    ),
    "Grilled Salmo": ItemData(
        classification=IC.useful,
        game_name="grilled-fish",
        item_type="Dish Recipie",
        item_id=1705,
    ),
    "Baked Prapple": ItemData(
        classification=IC.useful,
        game_name="baked-prapple",
        item_type="Dish Recipie",
        item_id=1706,
    ),
    "Prapple Salad": ItemData(
        classification=IC.useful,
        game_name="prapple-salad",
        item_type="Dish Recipie",
        pool_quantity=0,
        item_id=1707,
    ),
    "Pickled Garrot": ItemData(
        classification=IC.useful,
        game_name="pickled-garrot",
        item_type="Dish Recipie",
        item_id=1708,
    ),
    "Garrot Soup": ItemData(
        classification=IC.useful,
        game_name="carrot-soup",
        item_type="Dish Recipie",
        item_id=1709,
    ),
    "Fisher's Gift": ItemData(
        classification=IC.useful,
        game_name="smoked-fish",
        item_type="Dish Recipie",
        pool_quantity=0,
        item_id=1710,
    ),
    "Fieldfruit Bake": ItemData(
        classification=IC.useful,
        game_name="gartoffel-garrot",
        item_type="Dish Recipie",
        item_id=1711,
    ),
    "Up & Below": ItemData(
        classification=IC.useful,
        game_name="gartoffel-prapple",
        item_type="Dish Recipie",
        item_id=1712,
    ),
    "Clerry Roll": ItemData(
        classification=IC.useful,
        game_name="cloudberry-snack",
        item_type="Dish Recipie",
        item_id=1713,
    ),
    "Frumato Rice": ItemData(
        classification=IC.useful,
        game_name="frumato-rice",
        item_type="Dish Recipie",
        item_id=1714,
    ),
    "Shroomlett": ItemData(
        classification=IC.useful,
        game_name="shroom-egg",
        item_type="Dish Recipie",
        item_id=1715,
    ),
    "Swanana Nut Chips": ItemData(
        classification=IC.useful,
        game_name="banana-nut-chips",
        item_type="Dish Recipie",
        item_id=1716,
    ),
    "Sour Gugumber": ItemData(
        classification=IC.useful,
        game_name="sour-gugumber",
        item_type="Dish Recipie",
        item_id=1717,
    ),
}
