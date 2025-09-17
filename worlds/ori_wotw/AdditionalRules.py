"""Additional location rules that are not extracted from `areas.wotw`."""
from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import WotWWorld

def combat_rules(world: "WotWWorld"):
    """Defines rules for combat and light."""
    player = world.player
    options = world.options
    menu = world.get_region("Menu")
    diff = options.difficulty

    if diff == 0:  # Moki
        menu.connect(world.get_region("DepthsLight"),
                     rule=lambda state: state.has_any(("UpperDepths.ForestsEyes", "Flash"), player))
        menu.connect(world.get_region("Combat.Ranged"),
                     rule=lambda state: state.has_any(("Bow", "Spear"), player))
        menu.connect(world.get_region("Combat.Aerial"),
                     rule=lambda s: s.has_any(("Double Jump", "Launch"), player))
        menu.connect(world.get_region("Combat.Dangerous"),
                     rule=lambda s: s.has_any(("Double Jump", "Dash", "Bash", "Launch"), player))
        menu.connect(world.get_region("Combat.Shielded"),
                     rule=lambda s: s.has_any(("Hammer", "Launch", "Grenade", "Spear"), player))
        menu.connect(world.get_region("Combat.Bat"), rule=lambda s: s.has("Bash", player))
        menu.connect(world.get_region("Combat.Sand"), rule=lambda s: s.has("Burrow", player))
        menu.connect(world.get_region("BreakCrystal"),
                     rule=lambda s: s.has_any(("Sword", "Hammer", "Bow"), player))

    elif diff == 1:  # Gorlek
        menu.connect(world.get_region("DepthsLight"),
                     rule=lambda state: state.has_any(("UpperDepths.ForestsEyes", "Flash", "Bow"), player))
        menu.connect(world.get_region("Combat.Ranged"),
                     rule=lambda state: state.has_any(("Grenade", "Bow", "Shuriken", "Sentry", "Spear"), player))
        menu.connect(world.get_region("Combat.Aerial"),
                     rule=lambda s: s.has_any(("Double Jump", "Launch", "Bash"), player))
        menu.connect(world.get_region("Combat.Dangerous"),
                     rule=lambda s: s.has_any(("Double Jump", "Dash", "Bash", "Launch"), player))
        menu.connect(world.get_region("Combat.Shielded"),
                     rule=lambda s: s.has_any(("Hammer", "Launch", "Grenade", "Spear"), player))
        menu.connect(world.get_region("Combat.Bat"), rule=lambda s: s.has("Bash", player))
        menu.connect(world.get_region("Combat.Sand"), rule=lambda s: s.has("Burrow", player))
        menu.connect(world.get_region("BreakCrystal"),
                     rule=lambda s: s.has_any(("Sword", "Hammer", "Bow", "Shuriken", "Grenade"), player))

    elif diff == 2:  # Kii
        menu.connect(world.get_region("DepthsLight"),
                     rule=lambda state: state.has_any(("UpperDepths.ForestsEyes", "Flash", "Bow"), player))
        menu.connect(world.get_region("Combat.Ranged"),
                     rule=lambda state: state.has_any(("Grenade", "Bow", "Shuriken", "Sentry", "Spear"), player))
        menu.connect(world.get_region("Combat.Aerial"), rule=lambda s: True)
        menu.connect(world.get_region("Combat.Dangerous"),
                     rule=lambda s: s.has_any(("Double Jump", "Dash", "Bash", "Launch"), player))
        menu.connect(world.get_region("Combat.Shielded"),
                     rule=lambda s: s.has_any(("Hammer", "Launch", "Grenade", "Spear"), player))
        menu.connect(world.get_region("Combat.Bat"), rule=lambda s: True)
        menu.connect(world.get_region("Combat.Sand"), rule=lambda s: s.has("Burrow", player))
        menu.connect(world.get_region("BreakCrystal"),
                     rule=lambda s: s.has_any(("Sword", "Hammer", "Bow", "Shuriken", "Grenade"), player))

    else:  # Unsafe
        menu.connect(world.get_region("DepthsLight"),
                     rule=lambda state: state.has_any(("UpperDepths.ForestsEyes", "Flash", "Bow"), player))
        menu.connect(world.get_region("Combat.Ranged"),
                     rule=lambda state:
                     state.has_any(("Grenade", "Bow", "Shuriken", "Sentry", "Spear", "Blaze", "Flash"), player))
        menu.connect(world.get_region("Combat.Aerial"), rule=lambda s: True)
        menu.connect(world.get_region("Combat.Dangerous"),
                     rule=lambda s: s.has_any(("Double Jump", "Dash", "Bash", "Launch"), player))
        menu.connect(world.get_region("Combat.Shielded"),
                     rule=lambda s: s.has_any(("Hammer", "Launch", "Grenade", "Spear"), player))
        menu.connect(world.get_region("Combat.Bat"), rule=lambda s: True)
        menu.connect(world.get_region("Combat.Sand"), rule=lambda s: s.has("Burrow", player))
        menu.connect(world.get_region("BreakCrystal"),
                     rule=lambda s: s.has_any(("Sword", "Hammer", "Bow", "Shuriken", "Grenade", "Spear"), player))


def unreachable_rules(world: "WotWWorld"):
    """Rules to handle unreachable events."""
    player = world.player
    options = world.options
    diff = options.difficulty
    unreach: list[str]
    if diff == 0:
        unreach = ["WestHollow.AboveJumppad -> WestHollow.LowerTongueRetracted",
                   "OuterWellspring.EntranceDoor -> OuterWellspring.FallingWheel",
                   "MarshSpawn.PoolsBurrowsSignpost -> E.MarshSpawn.PoolsBurrowsSignpost",
                   "OuterWellspring.EntranceDoor -> H.OuterWellspring.EntranceDoor",
                   "OuterWellspring.EntranceDoor -> E.OuterWellspring.EntranceDoor",
                   "WoodsMain.TrialStart -> C.WoodsMain.TrialStart",
                   "WoodsMain.AbovePit -> E.WoodsMain.AbovePit",
                   "UpperReach.TreeRoom -> C.UpperReach.TreeRoom",
                   "UpperDepths.FirstKSRoom -> C.UpperDepths.FirstKSRoom",
                   "UpperDepths.FirstKSRoom -> E.UpperDepths.FirstKSRoom",
                   "UpperDepths.Central -> E.UpperDepths.Central",
                   "LowerDepths.West -> H.LowerDepths.West",
                   "LowerDepths.West -> E.LowerDepths.West",
                   "UpperWastes.MissilePuzzleMiddle -> C.UpperWastes.MissilePuzzleMiddle",
                   "WillowsEnd.Upper -> E.WillowsEnd.Upper"]
    elif diff == 1:
        unreach = ["OuterWellspring.EntranceDoor -> OuterWellspring.FallingWheel",
                   "MarshSpawn.PoolsBurrowsSignpost -> E.MarshSpawn.PoolsBurrowsSignpost",
                   "OuterWellspring.EntranceDoor -> E.OuterWellspring.EntranceDoor",
                   "WoodsMain.TrialStart -> C.WoodsMain.TrialStart",
                   "WoodsMain.AbovePit -> E.WoodsMain.AbovePit",
                   "UpperReach.TreeRoom -> C.UpperReach.TreeRoom",
                   "UpperDepths.FirstKSRoom -> C.UpperDepths.FirstKSRoom",
                   "UpperDepths.FirstKSRoom -> E.UpperDepths.FirstKSRoom",
                   "UpperDepths.Central -> E.UpperDepths.Central"]
    elif diff == 2:
        unreach = ["OuterWellspring.EntranceDoor -> OuterWellspring.FallingWheel",
                   "OuterWellspring.EntranceDoor -> E.OuterWellspring.EntranceDoor",
                   "WoodsMain.TrialStart -> C.WoodsMain.TrialStart",
                   "WoodsMain.AbovePit -> E.WoodsMain.AbovePit",
                   "UpperReach.TreeRoom -> C.UpperReach.TreeRoom",
                   "UpperDepths.FirstKSRoom -> C.UpperDepths.FirstKSRoom",
                   "UpperDepths.FirstKSRoom -> E.UpperDepths.FirstKSRoom",
                   "UpperDepths.Central -> E.UpperDepths.Central"]
    else:
        unreach = []

    for entr in unreach:  # Connect these events when the seed is completed, to make them reachable.
        set_rule(world.get_entrance(entr), lambda s: s.has("Victory", player))
