from .data_structures import DishData

dishes: dict[str, DishData] = {
    "Basic Ration": DishData(
            game_name="ration-basic",
        ),
    "Ring Ration": DishData(
        game_name="ration-ring",
    ),
    "Scrambled Egg": DishData(
        game_name="scrambled-egg",
    ),
    "Fried Rice": DishData(
        game_name="wild-rice-fried",
    ),
    "Ring Rolls": DishData(
        game_name="ring-rolls",
    ),
    "Grilled Salmo": DishData(
        game_name="grilled-fish",
    ),
    "Baked Prapple": DishData(
        game_name="baked-prapple",
    ),
    "Prapple Salad": DishData(
        game_name="prapple-salad",
    ),
    "Pickled Garrot": DishData(
        game_name="pickled-garrot",
    ),
    "Garrot Soup": DishData(
        game_name="carrot-soup",
    ),
    "Fisher's Gift": DishData(
        game_name="smoked-fish",
    ),
    "Fieldfruit Bake": DishData(
        game_name="gartoffel-garrot",
    ),
    "Up & Below": DishData(
        game_name="gartoffel-prapple",
    ),
    "Clerry Roll": DishData(
        game_name="cloudberry-snack",
    ),
    "Frumato Rice": DishData(
        game_name="frumato-rice",
    ),
}
