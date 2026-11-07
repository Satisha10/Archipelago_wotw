from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle, DefaultOnToggle, Choice


class SpawnMeleeWeapon(Choice):
    """Choose the starting melee weapon."""
    display_name = "Spawn Melee Weapon"
    option_sword = 0
    option_hammer = 1
    option_spear = 2
    default = 0


class SpawnRangeWeapon(Choice):
    """Choose the starting range weapon."""
    display_name = "Spawn Range Weapon"
    option_crossbow = 0
    option_chakram = 1
    option_kama = 2
    default = 0


class SpawnAspect(Choice):
    """Choose the starting aspect."""
    display_name = "Spawn Aspect"
    option_physis = 0
    option_aether = 1
    option_cryo = 2
    default = 0


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
    spawn_melee: SpawnMeleeWeapon
    spawn_range: SpawnRangeWeapon
    spawn_aspect: SpawnAspect
    quests: Quests
    divine_logic: DivineArtLogic
    craftsanity: Craftsanity
    cooksanity: Cooksanity

option_groups = [
    OptionGroup(
        "Starting items",
        [
            SpawnMeleeWeapon,
            SpawnRangeWeapon,
            SpawnAspect,
        ],
    ),
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
