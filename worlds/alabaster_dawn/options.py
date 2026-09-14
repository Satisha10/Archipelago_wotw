from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle, DefaultOnToggle


class Quests(DefaultOnToggle):
    """Add locations for side-quests."""
    display_name = "Quests"


class DivineArtLogic(Toggle):
    """Divine arts are logical ways to have blunt, pierce or slash access (outside of combat)."""
    display_name = "Divine Art Logic"


class Cooksanity(Toggle):
    """NOT IMPLEMENTED ! Add locations for cooking dishes and using spice."""
    display_name = "Cooksanity"


class Craftsanity(Toggle):
    """NOT IMPLEMENTED ! Add locations for crafting gems."""
    display_name = "Craftsanity"


@dataclass
class ADOptions(PerGameCommonOptions):
    quests: Quests
    divine_logic: DivineArtLogic
    craftsanity: Craftsanity
    cooksanity: Cooksanity

option_groups = [
    OptionGroup(
        "Logic changes",
        [
            DivineArtLogic,
        ],
    ),
    OptionGroup(
        "Location pool",
        [
            Quests,
            Cooksanity,
            Craftsanity,
        ],
    ),
]
