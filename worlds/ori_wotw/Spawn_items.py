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
               "WillowsEnd.InnerTP"]


def spawn_items(world, spawn, difficulty):
    """Returns a set of spawn items for the chosen spawn point and difficulty."""
    rand = world.random
    moki: List[List[List]] = [
            [["MarshTP"]],
            [["BurrowsTP", "Bash", "DoubleJump"],
             ["BurrowsTP", "Bash", "Dash"],
             ["BurrowsTP", "Bash", "Glide"]],
            [["DenTP", "DoubleJump"],
             ["DenTP", "Bash", "Grenade", "Sword"],
             ["DenTP", "Bash", "Grenade", "Hammer"]],
            [["HollowTP", "Sword", "Dash", "DoubleJump", "Regenerate", "Health", "Health", "Health", "Health"]],
            [["GladesTP", "DoubleJump", "Dash", "Bash"],
             ["GladesTP", "Water", "WaterDash"]],
            [["WellspringTP"]],
            [["WestWoodsTP", "Regenerate", "Health", "Health", "Health"]],
            [["EastWoodsTP", "DoubleJump", "Grapple", "Glide", "Regenerate", "Health", "Health", "Health"],
             ["EastWoodsTP", "Dash", "Grapple", "Glide", "Regenerate", "Health", "Health", "Health"]],
            [["ReachTP", "Flap", "DoubleJump", "Bash", "Grenade", "Regenerate", "Health", "Health", "Health"]],
            [["DepthsTP", "Glide", "Regenerate", "Health", "Health", "Health"]],
            [["EastPoolsTP", "Water", "Bash", "Regenerate", "Health", "Health", "Health"]],
            [["WestPoolsTP", "Water", "WaterDash", "WaterBreath", "Regenerate", "Health", "Health", "Health"]],
            [["WestWastesTP", "DoubleJump", "Grapple", "Regenerate", "Health", "Health", "Health", "Health",
              "Health"],
             ["WestWastesTP", "DoubleJump", "Burrow", "Regenerate", "Health", "Health", "Health", "Health",
              "Health"]],
            [["EastWastesTP", "Burrow", "Regenerate", "Health", "Health", "Health", "Health", "Health"]],
            [["OuterRuinsTP", "Burrow", "Regenerate", "Health", "Health", "Health", "Health", "Health"]],
            [["InnerRuinsTP", "Burrow", "DoubleJump", "Dash", "Grapple", "Regenerate", "Health", "Health", "Health",
              "Health", "Health"],
             ["InnerRuinsTP", "Burrow", "Glide", "Dash", "Grapple", "Regenerate", "Health", "Health",
              "Health", "Health", "Health"],
             ["InnerRuinsTP", "Burrow", "DoubleJump", "Glide", "Grapple", "Regenerate", "Health", "Health",
              "Health", "Health", "Health"]],
            [["WillowTP", "Launch", "200 SpiritLight", "Regenerate", "Health", "Health", "Health", "Health",
              "Health", "Health", "Health"]],
            ]

    gorlek: List[List[List]] = [
              [["MarshTP"]],
              [["BurrowsTP", "Bash", "DoubleJump"],
               ["BurrowsTP", "Bash", "Dash"],
               ["BurrowsTP", "Bash", "Glide"],
               ["BurrowsTP", "Bash", "Hammer"],
               ["BurrowsTP", "Bash", "Sword"]],
              [["DenTP", "DoubleJump"],
               ["DenTP", "Bash", "Grenade", "Sword"],
               ["DenTP", "Hammer"]],
              [["HollowTP", "Sword", "DoubleJump", "Bash", "Regenerate", "Health", "Health"],
               ["HollowTP", "Hammer", "DoubleJump", "Bash", "Regenerate", "Health", "Health"]],
              [["GladesTP", "DoubleJump", "Dash", "Bash"],
               ["GladesTP", "Water", "WaterDash"],
               ["GladesTP", "Water", "DoubleJump"],
               ["GladesTP", "Hammer"]],
              [["WellspringTP"]],
              [["WestWoodsTP", "Regenerate"]],
              [["EastWoodsTP", "DoubleJump", "Grapple", "Glide", "Regenerate"],
               ["EastWoodsTP", "Dash", "Grapple", "Glide", "Regenerate"]],
              [["ReachTP", "Flap", "DoubleJump", "Bash", "Grenade", "Regenerate"],
               ["ReachTP", "Flap", "Glide", "Grenade", "200 SpiritLight", "Regenerate"]],
              [["DepthsTP", "Glide", "Regenerate"]],
              [["EastPoolsTP", "Water", "Bash", "Regenerate"]],
              [["WestPoolsTP", "Water", "WaterDash", "Regenerate"]],
              [["WestWastesTP", "DoubleJump", "Grapple", "Regenerate"],
               ["WestWastesTP", "DoubleJump", "Burrow", "Regenerate"],
               ["WestWastesTP", "DoubleJump", "TripleJump", "Regenerate"],
               ["WestWastesTP", "Dash", "Grapple", "Regenerate"]],
              [["EastWastesTP", "Burrow", "Regenerate"]],
              [["OuterRuinsTP", "Burrow", "Regenerate"]],
              [["InnerRuinsTP", "Burrow", "DoubleJump", "Sword", "Grapple", "Regenerate"],
               ["InnerRuinsTP", "Burrow", "Glide", "Sword", "Grapple", "Regenerate"],
               ["InnerRuinsTP", "Burrow", "DoubleJump", "Hammer", "Grapple", "Regenerate"],
               ["InnerRuinsTP", "Burrow", "Glide", "Hammer", "Grapple", "Regenerate"]],
              [["WillowTP", "Launch", "200 SpiritLight", "Regenerate"]]
              ]

    kii: List[List[List]] = [
           [["MarshTP"]],
           [["BurrowsTP", "Bash"]],
           [["DenTP", "DoubleJump"],
            ["DenTP", "Sword", "Flash"],
            ["DenTP", "Sword", "Sentry"]],
           [["HollowTP", "Bash"],
            ["HollowTP", "Sword", "Grapple", "DoubleJump", "Regenerate", "Health", "Health"],
            ["HollowTP", "Hammer", "Grapple", "DoubleJump", "Regenerate", "Health", "Health"]],
           [["GladesTP", "Sword", "Bash"],
            ["GladesTP", "Water", "DoubleJump"],
            ["GladesTP", "Hammer"]],
           [["WellspringTP"]],
           [["WestWoodsTP", "Regenerate"]],
           [["EastWoodsTP", "DoubleJump", "Grapple", "Glide", "Regenerate"],
            ["EastWoodsTP", "Dash", "Grapple", "Glide", "Regenerate"],
            ["EastWoodsTP", "Dash", "DoubleJump", "Regenerate"]],
           [["ReachTP", "Flap", "DoubleJump", "Grenade", "Regenerate"],
            ["ReachTP", "Flap", "Bash", "Grenade", "Regenerate"]],
           [["DepthsTP", "Glide", "Regenerate"]],
           [["EastPoolsTP", "Water", "Regenerate"]],
           [["WestPoolsTP", "Water", "WaterDash", "Regenerate"]],
           [["WestWastesTP", "Hammer", "Grapple", "Regenerate"],
            ["WestWastesTP", "DoubleJump", "Sword", "Regenerate"],
            ["WestWastesTP", "DoubleJump", "TripleJump", "Regenerate"],
            ["WestWastesTP", "Dash", "Grapple", "Regenerate"]],
           [["EastWastesTP", "Burrow", "Regenerate"]],
           [["OuterRuinsTP", "Burrow", "Regenerate"]],
           [["InnerRuinsTP", "Burrow", "DoubleJump", "Dash", "Regenerate"],
            ["InnerRuinsTP", "Burrow", "Glide", "Grapple", "Regenerate"],
            ["InnerRuinsTP", "Burrow", "Hammer", "Dash", "Regenerate"],
            ["InnerRuinsTP", "Burrow", "DoubleJump", "Grapple", "Regenerate"]],
           [["WillowTP", "Launch", "200 SpiritLight", "Regenerate"]]
           ]

    unsafe: List[List[List]] = [
              [["MarshTP"]],
              [["BurrowsTP", "Bash"]],
              [["DenTP", "DoubleJump"],
               ["DenTP", "Sword"]],
              [["HollowTP", "Bash"],
               ["HollowTP", "Sword", "Grapple", "DoubleJump"],
               ["HollowTP", "Hammer", "DoubleJump"]],
              [["GladesTP", "Sword", "Bash"],
               ["GladesTP", "Water"],
               ["GladesTP", "Hammer"]],
              [["WellspringTP"]],
              [["WestWoodsTP"]],
              [["EastWoodsTP", "Grapple", "Glide"],
               ["EastWoodsTP", "Grapple", "Glide"],
               ["EastWoodsTP", "Dash", "DoubleJump"]],
              [["ReachTP", "Flap", "DoubleJump", "Grenade"],
               ["ReachTP", "Flap", "Bash", "Grenade"]],
              [["DepthsTP", "Glide"]],
              [["EastPoolsTP", "Water"]],
              [["WestPoolsTP", "Water", "WaterDash"]],
              [["WestWastesTP", "Hammer", "Grapple"],
               ["WestWastesTP", "DoubleJump"],
               ["WestWastesTP", "Dash", "Grapple"],
               ["WestWastesTP", "Sword", "Burrow"]],
              [["EastWastesTP", "Burrow"]],
              [["OuterRuinsTP", "Burrow"]],
              [["InnerRuinsTP", "Burrow", "DoubleJump", "Dash"],
               ["InnerRuinsTP", "Burrow", "Glide", "Grapple"],
               ["InnerRuinsTP", "Burrow", "Hammer", "Dash"],
               ["InnerRuinsTP", "Burrow", "DoubleJump", "Grapple"]],
              [["WillowTP", "Launch", "200 SpiritLight"]]
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
