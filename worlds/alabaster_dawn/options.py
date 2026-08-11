from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle, DefaultOnToggle


class Quests(DefaultOnToggle):
    """Add locations for side-quests."""
    display_name = "Quests"


class DivineSkillLogic(Toggle):
    """Divine skills are logical ways to have blunt, pierce or slash access."""
    display_name = "Divine Skill Logic"


class Cooksanity(Toggle):
    """Add locations for cooking dishes and using spice."""
    display_name = "Cooksanity"


class Craftsanity(Toggle):
    """Add locations for crafting gems."""
    display_name = "Craftsanity"


@dataclass
class ADOptions(PerGameCommonOptions):
    quests: Quests
    skill_logic: DivineSkillLogic
    craftsanity: Craftsanity
    cooksanity: Cooksanity

# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Logic changes",
        [
            DivineSkillLogic,
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
