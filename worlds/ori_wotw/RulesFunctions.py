from math import ceil, floor
from .Refills import refills
from worlds.AutoWorld import LogicMixin

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BaseClasses import CollectionState, MultiWorld
    from .Options import WotWOptions


# TODO Move combat events (dangerous, ranged...) here, and define a function that update the dict of enemy: defeatable
class WotWLogic(LogicMixin):
    """
    Class to store the max health/energy, refill values and defeatable enemies.

    All methods and variables should start with `wotw_`.
    """
    wotw_max_resources: dict[int, tuple[int, float]]  # Max health and energy
    wotw_refill_amount: dict[int, tuple[int, float]]  # Refill amounts for health and energy
    wotw_combat_tags: dict[int, set[str]]

    def init_mixin(self, mw: MultiWorld) -> None:
        self.wotw_max_resources = {player: (30, 3.0) for player in mw.get_game_players("Ori and the Will of the Wisps")}
        self.wotw_refill_amount = {player: (30, 1.0) for player in mw.get_game_players("Ori and the Will of the Wisps")}
        self.wotw_combat_tags = {player: set() for player in mw.get_game_players("Ori and the Will of the Wisps")}

# Rules for some glitches
def can_wavedash(state: CollectionState, player: int) -> bool:
    return state.has_all(("Dash", "Regenerate"), player)

def can_hammerjump(state: CollectionState, player: int) -> bool:
    return state.has_all(("Double Jump", "Hammer"), player)

def can_swordjump(state: CollectionState, player: int) -> bool:
    return state.has_all(("Double Jump", "Sword"), player)

def can_glidehammerjump(state: CollectionState, player: int) -> bool:
    return state.has_all(("Glide", "Hammer"), player)


weapon_data: dict[str, list] = {  # The list contains the damage, and its energy cost
    "Sword": [4, 0],
    "Hammer": [12, 0],
    "Grenade": [13, 1],  # Can be 17 damage if charged
    "Shuriken": [7, 0.5],
    "Bow": [4, 0.25],
    "Flash": [12, 1],
    "Sentry": [8, 1],  # 8.8, rounded down here
    "Spear": [20, 2],
    "Blaze": [13, 1],  # 13.8, rounded down here
    }


def get_max(state: CollectionState, player: int) -> tuple[int, float]:
    """Return the current max health and energy."""
    wisps = state.count_from_list(("EastHollow.ForestsVoice", "LowerReach.ForestsMemory", "UpperDepths.ForestsEyes",
                                  "WestPools.ForestsStrength", "WindtornRuins.Seir"), player)
    return (30 + state.count("Health Fragment", player)*5 + 10*wisps,
            3 + state.count("Energy Fragment", player)*0.5 + wisps)


def get_refill(state: CollectionState, player: int) -> tuple[int, int]:
    """Return the refill values."""
    max_h, max_e = state.wotw_max_resources[player]
    refill_h = min((4 + floor(max_h/50/0.6685)) * 10, max_h)
    refill_e = floor(max_e/5+1)
    return refill_h, refill_e


def can_enter_area(area: str, state: CollectionState, player: int, options: WotWOptions) -> bool:
    """Check if the requirement to enter an area is fulfilled."""
    difficulty = options.difficulty.value

    if area in ("MarshSpawn", "HowlsDen", "MarshPastOpher", "GladesTown"):  # No restriction in these areas
        return state.wotw_max_resources[player][0] > 30

    if difficulty == 3:  # Unsafe difficulty: no restriction
        return True

    area_data = {"MidnightBurrows": (25, False),  # For each area, minimum health and whether regenerate is needed
                 "EastHollow": (20, False),
                 "WestHollow": (20, False),
                 "WestGlades": (20, False),
                 "OuterWellspring": (25, False),
                 "InnerWellspring": (25, False),
                 "WoodsEntry": (40, True),
                 "WoodsMain": (40, True),
                 "LowerReach": (40, True),
                 "UpperReach": (40, True),
                 "UpperDepths": (40, True),
                 "LowerDepths": (40, True),
                 "PoolsApproach": (25, True),
                 "EastPools": (40, True),
                 "UpperPools": (40, True),
                 "WestPools": (40, True),
                 "LowerWastes": (50, True),
                 "UpperWastes": (50, True),
                 "WindtornRuins": (50, True),
                 "WeepingRidge": (60, True),
                 "WillowsEnd": (60, True),
                 }

    if difficulty != 0:  # Kii and Gorlek: only check for regenerate
        if area_data[area][1]:  # Kii, Gorlek
            return state.has("Regenerate", player)
        return True

    # Moki difficulty: check for health and regenerate
    if area_data[area][1]:
        return state.has("Regenerate", player) and state.wotw_max_resources[player][0] >= area_data[area][0]
    return state.wotw_max_resources[player][0] >= area_data[area][0]


def can_buy_map(state: CollectionState, player: int) -> bool:
    """Maps are logically required after collecting 1200 SL from 200 SL items."""
    return state.count("200 Spirit Light", player) >= 6


def can_open_door(state: CollectionState, player: int, door_name: str) -> bool:
    """
    Return if the door can be opened. The keystone (KS) costs are arbitrary.

    10 KS for early game doors that only require 2 KS to open.
    14 KS are mid-game doors that cost 2 KS (these doors are relevant early with random spawn).
    22 KS for mid-game doors at 4 KS.
    34 KS (enough KS to open everything) for doors that can be avoided or only lock a few items (and no trees).
    """
    keystone_data: dict[str, int] = {
        "MarshSpawn.KeystoneDoor": 10,
        "HowlsDen.KeystoneDoor": 10,
        "MarshPastOpher.EyestoneDoor": 10,
        "MidnightBurrows.KeystoneDoor": 34,
        "WoodsEntry.KeystoneDoor": 14,
        "WoodsMain.KeystoneDoor": 22,
        "LowerReach.KeystoneDoor": 34,
        "UpperReach.KeystoneDoor": 22,
        "UpperDepths.EntryKeystoneDoor": 14,
        "UpperDepths.CentralKeystoneDoor": 34,
        "UpperPools.KeystoneDoor": 22,
        "UpperWastes.KeystoneDoor": 14,
    }
    return state.count("Keystone", player) >= keystone_data[door_name]


# TODO Simplify with lists/dicts for and and or chains, with key is type of requirement, and then the value.
def cost_all(state: CollectionState, player: int, options: WotWOptions, region: str, damage_and: list,
             en_and: list[list], combat_and: list[list], or_req: list[list], path_difficulty: int) -> bool:
    """
    Return a bool stating if the path can be taken.

    damage_and: contains the dboost values (if several elements, Regenerate can be used inbetween).
    combat_and: contains the combat damages needed and the type (enemy/wall).
    en_and: contains as elements the skill name, and the amount used. All must be satisfied.
    or_req: contains damages, combat, and energy in each sublist (the first element of the list is the
        type of requirement: 0 is combat, 1 is energy, 2 is damage boost). Any can be verified.
    path_difficulty: 0, 1, 3, 5 for Moki, Gorlek, Kii, Unsafe
    """
    hard = options.hard_mode
    maxH, maxE = get_max(state, player)

    en, hp, tr = refills[region]  # TODO refills: typing, use tuples, use enum for refill type. Also split in a new function
    health, energy = 10, 1  # TODO: The base resources can lead to softlock, modify when resource tracking is reworked

    if path_difficulty == 0:  # Moki has no damage boost and barely requires energy, so this is fine.
        health, energy = maxH, maxE
    else:
        if tr == 2 and state.has("F." + region, player):
            health, energy = maxH, maxE
        else:
            if tr == 1 and state.has("C." + region, player):
                health, energy = get_refill((maxH, maxE))
            if hp != 0 and state.has("H." + region, player):
                health += hp*10
            if en != 0 and state.has("E." + region, player):
                energy += en

    # if diff != 3:  # Energy costs are doubled, except in unsafe
    #     energy /= 2

    for damage in damage_and:  # This part deals with the damage boosts
        if hard:
            damage *= 2
        health -= damage
        if health <= 0:
            if state.has("Regenerate", player) and -health < maxH:
                n_regen = ceil((-health + 1)/30)
                if n_regen > energy:
                    return False
                health = min(maxH, health + 30*n_regen)
                energy -= n_regen
            else:
                return False

    for source in en_and:  # This computes the energy cost for weapons
        if not state.has(source[0], player):
            return False
        energy -= weapon_data[source[0]][1] * source[1]
        if energy < 0:
            return False

    energy -= combat_cost(state, player, options, combat_and, bool(path_difficulty==0))
    if energy < 0:
        return False

    if or_req:
        min_cost = 1000  # Arbitrary value, higher than 20
        hp_cost = False
        for req in or_req:
            if req[0] == 0:
                if all([state.has(danger, player) for danger in req[2]]):
                    min_cost = min(min_cost, combat_cost(state, player, options, req[1], bool(path_difficulty==0)))
            if req[0] == 1:
                if state.has(req[1], player):
                    min_cost = min(min_cost, weapon_data[req[1]][1] * req[2])
            if req[0] == 2:
                hp_cost = req[1]
        if min_cost > energy:
            if not hp_cost:  # The damage boost option is considered only if no other option is possible.
                return False
            else:
                if hard:
                    hp_cost *= 2
                health -= hp_cost
                if state.has("Regenerate", player) and -health < maxH:  # Consider healing before the damage instance
                    n_regen = ceil((-health + 1)/30)
                    if n_regen > energy:  # In that case, not enough energy to heal
                        return False

    return True


def combat_cost(state: CollectionState, player: int, options: WotWOptions, hp_list: list[list],
                moki_path: bool) -> float:
    """Return the energy cost for the enemies/walls/boss with current state."""
    hard = options.hard_mode
    diff = options.difficulty
    if moki_path:
        if state.has_any(("Sword", "Hammer"), player):
            return 0
        return 1000  # Arbitrary value, greater than 200

    tot_cost = 0
    max_cost = 0  # Maximum amount used, in case there are refills during combat.
    for damage, category in hp_list:
        if category == "Combat":
            if diff == 3:
                weapons = ["Sword", "Hammer", "Grenade", "Bow", "Shuriken", "Sentry", "Spear", "Blaze", "Flash"]
            else:
                weapons = ["Sword", "Hammer", "Grenade", "Bow", "Shuriken", "Sentry", "Spear", "Blaze"]
        elif category == "Wall":
            weapons = ["Sword", "Hammer", "Grenade", "Bow", "Shuriken", "Sentry", "Spear", "Blaze"]
        elif category == "Boss":
            if hard:
                damage *= 1.8
            if diff == 3:
                weapons = ["Sword", "Hammer", "Grenade", "Bow", "Shuriken", "Sentry", "Spear", "Blaze", "Flash"]
            else:
                weapons = ["Sword", "Hammer", "Grenade", "Bow", "Shuriken", "Sentry", "Spear", "Blaze"]
        elif category == "Refill":
            max_cost = max(max_cost, tot_cost)
            tot_cost -= damage  # In that case, damage contains the amount of energy given back
            continue
        else:  # ShurikenBreak or SentryBreak
            weapons = [category]

        cost = 1000  # Arbitrary value, higher than 20
        for weapon in weapons:
            if state.has(weapon, player):
                cost = min(cost, weapon_data[weapon][1] * ceil(damage / weapon_data[weapon][0]))
        tot_cost += cost

    return max(tot_cost, max_cost)
