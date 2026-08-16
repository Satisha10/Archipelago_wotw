from BaseClasses import ItemClassification as IC

from ..data_structures import ItemData

blueprints: dict[str, ItemData] = {
    "Blood Eye Construct": ItemData(
        classification=IC.useful,
        game_name="bp-mel-min-aff",
        item_type="Construct",
    ),
    "Shatter End Construct": ItemData(
        classification=IC.useful,
        game_name="bp-mel-min-breaker",
        item_type="Construct",
    ),
    "Amplifier Construct": ItemData(
        classification=IC.useful,
        game_name="bp-mel-min-ampli",
        item_type="Construct",
    ),
    "Finishing Touch Construct": ItemData(
        classification=IC.useful,
        game_name="bp-mel-finisher",
        item_type="Construct",
    ),
    "Double Trouble Construct": ItemData(
        classification=IC.useful,
        game_name="bp-mel-brkdmg",
        item_type="Construct",
    ),
    "Distant Mark Construct": ItemData(
        classification=IC.useful,
        game_name="bp-rang-min-snip",
        item_type="Construct",
    ),
    "High Ground Construct": ItemData(
        classification=IC.useful,
        game_name="bp-rang-min-highground",
        item_type="Construct",
    ),
    "Fly Swatter Construct": ItemData(
        classification=IC.useful,
        game_name="bp-rng-min-wing",
        item_type="Construct",
    ),
    "Stem Pecker Construct": ItemData(
        classification=IC.useful,
        game_name="bp-rng-min-root",
        item_type="Construct",
    ),
    "Bully Construct": ItemData(
        classification=IC.useful,
        game_name="bp-rng-min-bul",
        item_type="Construct",
    ),
    "Steady Zeal Construct": ItemData(
        classification=IC.useful,
        game_name="bp-rng-min-dp",
        item_type="Construct",
    ),
    "Verdant Guard Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-defl",
        item_type="Construct",
    ),
    "Libra's Blessing Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-aether",
        item_type="Construct",
    ),
    "Blood Heart Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-crit",
        item_type="Construct",
    ),
    "Tireless Boulder Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-stam",
        item_type="Construct",
    ),
    "Lucky Reflex Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-critdef",
        item_type="Construct",
    ),
    "Feline's Gaze Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-hazdef",
        item_type="Construct",
    ),
    "Grit Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-grit",
        item_type="Construct",
    ),
    "Cleanse Construct": ItemData(
        classification=IC.useful,
        game_name="bp-cor-min-balance",
        item_type="Construct",
    ),
    # TODO Blueprints
}
