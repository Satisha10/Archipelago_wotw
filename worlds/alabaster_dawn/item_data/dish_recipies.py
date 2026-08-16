from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

dish: dict[str, ItemData] = {
    "Basic Ration": ItemData(
        classification=IC.useful,
        game_name="ration-basic",
        item_type="Dish Recipie",
    ),
    "Ring Ration": ItemData(
        classification=IC.useful,
        game_name="ration-ring",
        item_type="Dish Recipie",
    ),
    "Scrambled Egg": ItemData(
        classification=IC.useful,
        game_name="scrambled-egg",
        item_type="Dish Recipie",
    ),
    "Fried Rice": ItemData(
        classification=IC.useful,
        game_name="wild-rice-fried",
        item_type="Dish Recipie",
    ),
    "Ring Rolls": ItemData(
        classification=IC.useful,
        game_name="ring-rolls",
        item_type="Dish Recipie",
    ),
    "Grilled Salmo": ItemData(
        classification=IC.useful,
        game_name="grilled-fish",
        item_type="Dish Recipie",
    ),
    "Baked Prapple": ItemData(
        classification=IC.useful,
        game_name="baked-prapple",
        item_type="Dish Recipie",
    ),
    "Prapple Salad": ItemData(
        classification=IC.useful,
        game_name="prapple-salad",
        item_type="Dish Recipie",
    ),
    "Pickled Garrot": ItemData(
        classification=IC.useful,
        game_name="pickled-garrot",
        item_type="Dish Recipie",
    ),
    "Garrot Soup": ItemData(
        classification=IC.useful,
        game_name="carrot-soup",
        item_type="Dish Recipie",
    ),
    "Fisher's Gift": ItemData(
        classification=IC.useful,
        game_name="smoked-fish",
        item_type="Dish Recipie",
    ),
    "Fieldfruit Bake": ItemData(
        classification=IC.useful,
        game_name="gartoffel-garrot",
        item_type="Dish Recipie",
    ),
    "Up & Below": ItemData(
        classification=IC.useful,
        game_name="gartoffel-prapple",
        item_type="Dish Recipie",
    ),
    "Clerry Roll": ItemData(
        classification=IC.useful,
        game_name="cloudberry-snack",
        item_type="Dish Recipie",
    ),
    "Frumato Rice": ItemData(
        classification=IC.useful,
        game_name="frumato-rice",
        item_type="Dish Recipie",
    ),
}
