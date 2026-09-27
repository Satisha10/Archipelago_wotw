"""Locations for cooking dishes. Location ID Band: 2000-2199"""

from .data_structures import DishData

dishes: dict[str, DishData] = {
    "Basic Ration": DishData(
        game_name="ration-basic",
        loc_id=2000,
    ),
    "Ring Ration": DishData(
        game_name="ration-ring",
        loc_id=2001,
    ),
    "Scrambled Egg": DishData(
        game_name="scrambled-egg",
        loc_id=2002,
    ),
    "Fried Rice": DishData(
        game_name="wild-rice-fried",
        loc_id=2003,
    ),
    "Ring Rolls": DishData(
        game_name="ring-rolls",
        loc_id=2004,
    ),
    "Grilled Salmo": DishData(
        game_name="grilled-fish",
        loc_id=2005,
    ),
    "Baked Prapple": DishData(
        game_name="baked-prapple",
        loc_id=2006,
    ),
    "Prapple Salad": DishData(
        game_name="prapple-salad",
        loc_id=2007,
    ),
    "Pickled Garrot": DishData(
        game_name="pickled-garrot",
        loc_id=2008,
    ),
    "Garrot Soup": DishData(
        game_name="carrot-soup",
        loc_id=2009,
    ),
    "Fisher's Gift": DishData(
        game_name="smoked-fish",
        loc_id=2010,
    ),
    "Fieldfruit Bake": DishData(
        game_name="gartoffel-garrot",
        loc_id=2011,
    ),
    "Up & Below": DishData(
        game_name="gartoffel-prapple",
        loc_id=2012,
    ),
    "Clerry Roll": DishData(
        game_name="cloudberry-snack",
        loc_id=2013,
    ),
    "Frumato Rice": DishData(
        game_name="frumato-rice",
        loc_id=2014,
    ),
}
