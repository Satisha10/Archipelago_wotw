from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Toggle, DefaultOnToggle, Choice, Range


class WeaveGoalAmount(Range):
    """How many Nyx Nests or Spires are required to weave before goaling."""
    display_name = "Weave Goal Amount"
    range_start = 1
    range_end = 5
    default = 5


class ProgressiveAreas(Choice):
    """
    Turn area and dungeon unlocks into progressive items. The order is the vanilla progression from the story.

    - **false**: each area has its own item to be unlocked.
    - **split**: add Overworld Area unlock and Dungeon unlock items.
    - **combine**: add Area unlock items that unlock both dungeons and areas.
    """
    display_name = "Progressive Area Unlocks"
    option_false = 0
    option_split = 1
    option_combine = 2
    default = 2


class MasterKeys(Toggle):
    """Add only one key per dungeon in the item pool which can open every door, instead of multiple keys."""
    display_name = "Master Dungeon Keys"


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


class SpawnWithRelics(Toggle):
    """Receive relics on spawn, otherwise they are added as items."""
    display_name = "Spawn with Relics"


class Quests(DefaultOnToggle):
    """Add locations for side-quests."""
    display_name = "Quests"


class DivineArtLogic(Toggle):
    """Divine arts are logical ways to have blunt, pierce or slash access (outside of combat)."""
    display_name = "Divine Art Logic"


class ChestHints(Choice):
    """
    Show the classification of the items contained in the chests (on the map and in the chest appearance).
    - **never**: the classification is never shown.
    - **seen**: only show the hint once the chest appeared on screen once.
    - **always**: always show the hints for all chests.
    """
    display_name = "Chest Hints"
    option_never = 0
    option_seen = 1
    option_always = 2
    default = 1


class Cooksanity(Toggle):
    """NOT IMPLEMENTED ! Add locations for cooking dishes and using spice."""
    display_name = "Cooksanity"


class Craftsanity(Toggle):
    """NOT IMPLEMENTED ! Add locations for crafting gems."""
    display_name = "Craftsanity"


@dataclass
class ADOptions(PerGameCommonOptions):
    weave_goal: WeaveGoalAmount
    progressive_areas: ProgressiveAreas
    spawn_melee: SpawnMeleeWeapon
    spawn_range: SpawnRangeWeapon
    spawn_aspect: SpawnAspect
    spawn_relics: SpawnWithRelics
    master_keys: MasterKeys
    quests: Quests
    divine_logic: DivineArtLogic
    chest_hints: ChestHints
    craftsanity: Craftsanity
    cooksanity: Cooksanity

option_groups = [
    OptionGroup(
        "Goal",
        [
            WeaveGoalAmount,
        ]
    ),
    OptionGroup(
        "Items",
        [
            ProgressiveAreas,
            MasterKeys,
        ],
    ),
    OptionGroup(
        "Starting items",
        [
            SpawnMeleeWeapon,
            SpawnRangeWeapon,
            SpawnAspect,
            SpawnWithRelics,
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
    OptionGroup(
        "Hints",
        [
            ChestHints
        ],
    ),
]
