"""Function for handling spawn items for random spawn."""

from typing import List

spawn_names = ["MarshSpawn.Main",
               "MidnightBurrows.Teleporter",
               "HowlsDen.Teleporter",
               "EastHollow.Teleporter",
               "GladesTown.Teleporter",
               "InnerWellspring.Teleporter",
               "WoodsEntry.Teleporter",
               "WoodsMain.Teleporter",
               "LowerReach.Teleporter",
               "UpperDepths.Teleporter",
               "EastPools.Teleporter",
               "WestPools.Teleporter",
               "LowerWastes.WestTP",
               "LowerWastes.EastTP",
               "UpperWastes.NorthTP",
               "WindtornRuins.RuinsTP",
               "WillowsEnd.InnerTP",]


def spawn_items(world, spawn, difficulty):
    """
    Returns a set of spawn items for the chosen spawn point and difficulty.

    The items are stored in a list of dimension 3 for each difficulty ;
    with spawn location, item groups, items along 1st, 2nd, 3rd indexes respectively.
    """
    rand = world.random
    moki: List[List[List]] = [
            [["Inkwater Marsh TP"]],
            [["Midnight Burrows TP", "Bash", "Double Jump"],
             ["Midnight Burrows TP", "Bash", "Dash"],
             ["Midnight Burrows TP", "Bash", "Glide"]],
            [["Howl's Den TP", "Double Jump"],
             ["Howl's Den TP", "Bash", "Grenade", "Sword"],
             ["Howl's Den TP", "Bash", "Grenade", "Hammer"]],
            [["Kwolok's Hollow TP", "Sword", "Dash", "Double Jump", "Regenerate", "Health", "Health", "Health",
              "Health"]],
            [["Glades TP", "Double Jump", "Dash", "Bash"],
             ["Glades TP", "Water", "Water Dash"]],
            [["Wellspring TP"]],
            [["Woods Entrance TP", "Regenerate", "Health", "Health", "Health"]],
            [["Woods Exit TP", "Double Jump", "Grapple", "Glide", "Regenerate", "Health", "Health", "Health"],
             ["Woods Exit TP", "Dash", "Grapple", "Glide", "Regenerate", "Health", "Health", "Health"]],
            [["Baur's Reach TP", "Flap", "Double Jump", "Bash", "Grenade", "Regenerate", "Health", "Health", "Health"]],
            [["Mouldwood Depths TP", "Glide", "Regenerate", "Health", "Health", "Health"]],
            [["Central Luma TP", "Water", "Bash", "Regenerate", "Health", "Health", "Health"]],
            [["Luma Boss TP", "Water", "Water Dash", "Water Breath", "Regenerate", "Health", "Health", "Health"]],
            [["Feeding Grounds TP", "Double Jump", "Grapple", "Regenerate", "Health", "Health", "Health", "Health",
              "Health"],
             ["Feeding Grounds TP", "Double Jump", "Burrow", "Regenerate", "Health", "Health", "Health", "Health",
              "Health"]],
            [["Central Wastes TP", "Burrow", "Regenerate", "Health", "Health", "Health", "Health", "Health"]],
            [["Outer Ruins TP", "Burrow", "Regenerate", "Health", "Health", "Health", "Health", "Health"]],
            [["Inner Ruins TP", "Burrow", "Double Jump", "Dash", "Grapple", "Regenerate", "Health", "Health", "Health",
              "Health", "Health"],
             ["Inner Ruins TP", "Burrow", "Glide", "Dash", "Grapple", "Regenerate", "Health", "Health",
              "Health", "Health", "Health"],
             ["Inner Ruins TP", "Burrow", "Double Jump", "Glide", "Grapple", "Regenerate", "Health", "Health",
              "Health", "Health", "Health"]],
            [["Willow's End TP", "Launch", "200 Spirit Light", "200 Spirit Light", "Regenerate", "Health", "Health",
              "Health", "Health", "Health", "Health", "Health"]],
            ]

    gorlek: List[List[List]] = [
              [["Inkwater Marsh TP"]],
              [["Midnight Burrows TP", "Bash", "Double Jump"],
               ["Midnight Burrows TP", "Bash", "Dash"],
               ["Midnight Burrows TP", "Bash", "Glide"],
               ["Midnight Burrows TP", "Bash", "Hammer"],
               ["Midnight Burrows TP", "Bash", "Sword"]],
              [["Howl's Den TP", "Double Jump"],
               ["Howl's Den TP", "Bash", "Grenade", "Sword"],
               ["Howl's Den TP", "Hammer"]],
              [["Kwolok's Hollow TP", "Sword", "Double Jump", "Bash", "Regenerate", "Health", "Health"],
               ["Kwolok's Hollow TP", "Hammer", "Double Jump", "Bash", "Regenerate", "Health", "Health"]],
              [["Glades TP", "Double Jump", "Dash", "Bash"],
               ["Glades TP", "Water", "Water Dash"],
               ["Glades TP", "Water", "Double Jump"],
               ["Glades TP", "Hammer"]],
              [["Wellspring TP"]],
              [["Woods Entrance TP", "Regenerate"]],
              [["Woods Exit TP", "Double Jump", "Grapple", "Glide", "Regenerate"],
               ["Woods Exit TP", "Dash", "Grapple", "Glide", "Regenerate"]],
              [["Baur's Reach TP", "Flap", "Double Jump", "Bash", "Grenade", "Regenerate"],
               ["Baur's Reach TP", "Flap", "Glide", "Grenade", "200 Spirit Light", "200 Spirit Light", "Regenerate"]],
              [["Mouldwood Depths TP", "Glide", "Regenerate"]],
              [["Central Luma TP", "Water", "Bash", "Regenerate"]],
              [["Luma Boss TP", "Water", "Water Dash", "Regenerate"]],
              [["Feeding Grounds TP", "Double Jump", "Grapple", "Regenerate"],
               ["Feeding Grounds TP", "Double Jump", "Burrow", "Regenerate"],
               ["Feeding Grounds TP", "Double Jump", "TripleJump", "Regenerate"],
               ["Feeding Grounds TP", "Dash", "Grapple", "Regenerate"]],
              [["Central Wastes TP", "Burrow", "Regenerate"]],
              [["Outer Ruins TP", "Burrow", "Regenerate"]],
              [["Inner Ruins TP", "Burrow", "Double Jump", "Sword", "Grapple", "Regenerate"],
               ["Inner Ruins TP", "Burrow", "Glide", "Sword", "Grapple", "Regenerate"],
               ["Inner Ruins TP", "Burrow", "Double Jump", "Hammer", "Grapple", "Regenerate"],
               ["Inner Ruins TP", "Burrow", "Glide", "Hammer", "Grapple", "Regenerate"]],
              [["Willow's End TP", "Launch", "200 Spirit Light", "200 Spirit Light", "Regenerate"]],
              ]

    kii: List[List[List]] = [
           [["Inkwater Marsh TP"]],
           [["Midnight Burrows TP", "Bash"]],
           [["Howl's Den TP", "Double Jump"],
            ["Howl's Den TP", "Sword", "Flash"],
            ["Howl's Den TP", "Sword", "Sentry"]],
           [["Kwolok's Hollow TP", "Bash"],
            ["Kwolok's Hollow TP", "Sword", "Grapple", "Double Jump", "Regenerate", "Health", "Health"],
            ["Kwolok's Hollow TP", "Hammer", "Grapple", "Double Jump", "Regenerate", "Health", "Health"]],
           [["Glades TP", "Sword", "Bash"],
            ["Glades TP", "Water", "Double Jump"],
            ["Glades TP", "Hammer"]],
           [["Wellspring TP"]],
           [["Woods Entrance TP", "Regenerate"]],
           [["Woods Exit TP", "Double Jump", "Grapple", "Glide", "Regenerate"],
            ["Woods Exit TP", "Dash", "Grapple", "Glide", "Regenerate"],
            ["Woods Exit TP", "Dash", "Double Jump", "Regenerate"]],
           [["Baur's Reach TP", "Flap", "Double Jump", "Grenade", "Regenerate"],
            ["Baur's Reach TP", "Flap", "Bash", "Grenade", "Regenerate"]],
           [["Mouldwood Depths TP", "Glide", "Regenerate"]],
           [["Central Luma TP", "Water", "Regenerate"]],
           [["Luma Boss TP", "Water", "Water Dash", "Regenerate"]],
           [["Feeding Grounds TP", "Hammer", "Grapple", "Regenerate"],
            ["Feeding Grounds TP", "Double Jump", "Sword", "Regenerate"],
            ["Feeding Grounds TP", "Double Jump", "TripleJump", "Regenerate"],
            ["Feeding Grounds TP", "Dash", "Grapple", "Regenerate"]],
           [["Central Wastes TP", "Burrow", "Regenerate"]],
           [["Outer Ruins TP", "Burrow", "Regenerate"]],
           [["Inner Ruins TP", "Burrow", "Double Jump", "Dash", "Regenerate"],
            ["Inner Ruins TP", "Burrow", "Glide", "Grapple", "Regenerate"],
            ["Inner Ruins TP", "Burrow", "Hammer", "Dash", "Regenerate"],
            ["Inner Ruins TP", "Burrow", "Double Jump", "Grapple", "Regenerate"]],
           [["Willow's End TP", "Launch", "200 Spirit Light", "200 Spirit Light", "Regenerate"]],
           ]

    unsafe: List[List[List]] = [
              [["Inkwater Marsh TP"]],
              [["Midnight Burrows TP", "Bash"]],
              [["Howl's Den TP", "Double Jump"],
               ["Howl's Den TP", "Sword"]],
              [["Kwolok's Hollow TP", "Bash"],
               ["Kwolok's Hollow TP", "Sword", "Grapple", "Double Jump"],
               ["Kwolok's Hollow TP", "Hammer", "Double Jump"]],
              [["Glades TP", "Sword", "Bash"],
               ["Glades TP", "Water"],
               ["Glades TP", "Hammer"]],
              [["Wellspring TP"]],
              [["Woods Entrance TP"]],
              [["Woods Exit TP", "Grapple", "Glide"],
               ["Woods Exit TP", "Grapple", "Glide"],
               ["Woods Exit TP", "Dash", "Double Jump"]],
              [["Baur's Reach TP", "Flap", "Double Jump", "Grenade"],
               ["Baur's Reach TP", "Flap", "Bash", "Grenade"]],
              [["Mouldwood Depths TP", "Glide"]],
              [["Central Luma TP", "Water"]],
              [["Luma Boss TP", "Water", "Water Dash"]],
              [["Feeding Grounds TP", "Hammer", "Grapple"],
               ["Feeding Grounds TP", "Double Jump"],
               ["Feeding Grounds TP", "Dash", "Grapple"],
               ["Feeding Grounds TP", "Sword", "Burrow"]],
              [["Central Wastes TP", "Burrow"]],
              [["Outer Ruins TP", "Burrow"]],
              [["Inner Ruins TP", "Burrow", "Double Jump", "Dash"],
               ["Inner Ruins TP", "Burrow", "Glide", "Grapple"],
               ["Inner Ruins TP", "Burrow", "Hammer", "Dash"],
               ["Inner Ruins TP", "Burrow", "Double Jump", "Grapple"]],
              [["Willow's End TP", "Launch", "200 Spirit Light", "200 Spirit Light"]],
              ]

    if difficulty == 0:
        sets: List[List] = moki[spawn]
    elif difficulty == 1 or difficulty == 2:
        sets: List[List] = gorlek[spawn]
    elif difficulty == 3 or difficulty == 4:
        sets: List[List] = kii[spawn]
    else:
        sets: List[List] = unsafe[spawn]
    i = rand.randrange(len(sets))
    return sets[i]
