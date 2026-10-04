"""Chests. Location ID Band: 200-1499"""

from rule_builder.rules import Has, HasAll

from .data_structures import ChestData
from .rule_helpers import has_any_elements

# TODO for any_elements, check if aether or physis are explicitly required

chests: dict[str, ChestData] = {
    "Plains.Somu.West": ChestData(
        game_name="hub.west-01-1",
        area="Aurum Plains",
        rule=Has("Kama"),
        loc_id=330,
    ),
    "Plains.Somu.East": ChestData(
        game_name="hub.west-01-2",
        area="Aurum Plains",
        rule=HasAll("Kama", "Cryo"),
        loc_id=349,
    ),
    "Plains.Watchtower": ChestData(
        game_name="hub.south-01-1",
        area="Aurum Plains",
        rule=Has("Kama"),
        loc_id=331,
    ),
    "Plains.HiddenSteep.West": ChestData(
        game_name="hub.south-03-1",
        area="Aurum Plains",
        rule=Has("Kama"),
        loc_id=332,
    ),
    "Plains.HiddenSteep.SouthEast": ChestData(
        game_name="hub.south-03-2",
        area="Aurum Plains",
        rule=HasAll("Aether", "Chakram", "Filia"),
        loc_id=333,
    ),
    "Plains.HiddenSteep.Hidden": ChestData(
        game_name="hub.south-03-3",
        area="Aurum Plains",
        loc_id=334,
    ),
    "Plains.RiverRoad.Statue": ChestData(
        game_name="hub.south-04-1",
        area="Aurum Plains",
        loc_id=335,
    ),
    "Plains.RiverRoad.NorthEast": ChestData(
        game_name="hub.south-04-2",
        area="Aurum Plains",
        rule=HasAll("Filia", "Range"),
        loc_id=336,
    ),
    "Plains.RiverRoad.North": ChestData(
        game_name="hub.south-04-3",
        area="Aurum Plains",
        loc_id=337,
    ),
    "Plains.OldFarm.East": ChestData(
        game_name="hub.north-01-1",
        area="Aurum Plains",
        rule=Has("Range"),
        loc_id=338,
    ),
    "Plains.OldFarm.SouthWest": ChestData(
        game_name="hub.north-01-2",
        area="Aurum Plains",
        loc_id=339,
    ),
    "Plains.OldFarm.West": ChestData(
        game_name="hub.north-01-3",
        area="Aurum Plains",
        loc_id=340,
    ),
    "Plains.NorthBend.North": ChestData(
        game_name="hub.north-02-1",
        area="Aurum Plains",
        rule=HasAll("Blunt", "Combat"),
        loc_id=341,
    ),
    "Plains.ImpactCrater": ChestData(
        game_name="hub.north-04-1",
        area="Aurum Plains",
        loc_id=350,
    ),
    "Plains.RuinedRanch.West": ChestData(
        game_name="hub.north-05-1",
        area="Aurum Plains",
        rule=HasAll("Kama", "Filia", "Aether"),  # Aether for combat ?
        loc_id=342,
    ),
    "Plains.SouthBend.West": ChestData(
        game_name="hub.center-06-1",
        area="Aurum Plains",
        rule=HasAll("Kama", "Filia", "Aether", "Chakram"),  # Need to solve the big puzzle before
        loc_id=343,
    ),
    "Plains.SouthBend.East": ChestData(
        game_name="hub.center-06-2",
        area="Aurum Plains",
        loc_id=344,
    ),
    "Plains.SouthBend.North": ChestData(
        game_name="hub.center-06-3",
        area="Aurum Plains",
        rule=Has("Range"),
        loc_id=345,
    ),
    "Sundalan.Meridi": ChestData(
        game_name="hub.town-south-1",
        area="Sundalan",
        loc_id=346,
    ),
    "Plains.SolGate": ChestData(
        game_name="hub.bridge-01-1",
        area="Aurum Plains",
        loc_id=347,
    ),
    "Plains.SolGate.Puzzle": ChestData(
        game_name="hub.bridge-01-puzzle-01",
        area="Aurum Plains",
        rule=HasAll("Chakram", "Aether", "Filia") & Has("Fulcrum Mark", count=2) & has_any_elements(2),
        loc_id=348,
    ),
    "Valley.ForkedRoad.East": ChestData(
        game_name="start.center-01-1",
        area="Koro Valley",
        rule=HasAll("Aether", "Range"),
        loc_id=200,
    ),
    "Valley.ForkedRoad.West": ChestData(
        game_name="start.center-01-2",
        area="Koro Valley",
        rule=HasAll("Aether", "Range", "Blunt"),
        loc_id=201,
    ),
    "Valley.ForkedRoad.South": ChestData(
        game_name="start.center-01-3",
        area="Koro Valley",
        loc_id=202,
    ),
    "Valley.ReaversEnd.North": ChestData(
        game_name="start.center-02-1",
        area="Koro Valley",
        rule=HasAll("Blunt", "Range"),  # Requires the combat
        loc_id=203,
    ),
    "Valley.ReaversEnd.East": ChestData(
        game_name="start.center-02-2",
        area="Koro Valley",
        rule=HasAll("Chakram", "Blunt"),
        loc_id=204,
    ),
    "Valley.ReaversEnd.Boss": ChestData(
        game_name="start.center-02-3",
        area="Koro Valley",
        rule=HasAll("Blunt", "Range"),
        loc_id=205,
    ),
    "Valley.EyeRemis": ChestData(
        game_name="start.center-03-2",
        area="Koro Valley",
        loc_id=206,
    ),
    "Valley.Kamu.West": ChestData(
        game_name="start.center-04-1",
        area="Koro Valley",
        rule=HasAll("Blunt", "Combat"),
        loc_id=207,
    ),
    "Valley.Kamu.NorthEast": ChestData(
        game_name="start.center-04-2",
        area="Koro Valley",
        rule=Has("Blunt"),
        loc_id=208,
    ),
    "Valley.Kamu.South": ChestData(
        game_name="start.center-04-3",
        area="Koro Valley",
        rule=Has("Chakram"),
        loc_id=209,
    ),
    "Valley.Fossil.South": ChestData(
        game_name="start.center-05-1",
        area="Koro Valley",
        loc_id=210,
    ),
    "Valley.Fossil.East": ChestData(
        game_name="start.center-05-2",
        area="Koro Valley",
        rule=HasAll("Filia", "Aether", "Range"),
        loc_id=211,
    ),
    "Valley.Lumber.EternalSpringChest": ChestData(
        game_name="start.center-06-1",
        area="Koro Valley",  # TODO requires to hit a switch in melee
        loc_id=212,
    ),
    "Valley.Lumber.West": ChestData(
        game_name="start.center-06-2",
        area="Koro Valley",
        loc_id=213,
    ),
    "Valley.Lumber.East": ChestData(
        game_name="start.center-06-3",
        area="Koro Valley",
        rule=Has("Range"),
        loc_id=214,
    ),
    "Valley.LyhamnShelter.East": ChestData(
        game_name="start.center-07-1",
        area="Koro Valley",
        rule=HasAll("Kama", "Pierce"),
        loc_id=215,
    ),
    "Valley.LyhamnShelter.Combat": ChestData(
        game_name="start.center-07-2",
        area="Koro Valley",
        loc_id=216,
    ),
    "EternalSpring.Outside": ChestData(
        game_name="start.center-08-1",
        area="Eternal Spring",
        rule=has_any_elements(2) & Has("Pierce Range"),  # TODO check that it is only reachable once dng complete
        loc_id=217,
    ),  # The rules are for completing the dungeon, most of them are in the area rule
    "Valley.Crescent.SouthWest": ChestData(
        game_name="start.north-01-2",
        area="Koro Valley",
        rule=Has("Valley bridges"),
        loc_id=218,
    ),
    "Valley.Crescent.East": ChestData(  # TODO We'll need to nerf the level or exclude the location on that one
        game_name="start.north-01-3",
        area="Aurum Plains",
        rule=Has("Slash Combat"),
        loc_id=256,
    ),
    "Valley.Crescent.South": ChestData(
        game_name="start.north-01-1",
        area="Aurum Plains",
        loc_id=257,
    ),
    "Valley.ValleyEntrance.Bridge": ChestData(
        game_name="start.north-02-1",
        area="Koro Valley North",
        loc_id=219,
    ),
    "Valley.ValleyEntrance.East": ChestData(
        game_name="start.north-02-2",
        area="Koro Valley North",
        rule=Has("Range"),
        loc_id=220,
    ),
    "Valley.DuskApproach.East": ChestData(
        game_name="start.north-03-1",
        area="Koro Valley North",
        rule=Has("Kama"),
        loc_id=221,
    ),
    "Valley.DuskApproach.South": ChestData(  # Missable in 0.1.0, but might be ok if tide is an item
        game_name="start.north-03-2",
        area="Koro Valley North",
        rule=Has("Low tide"),
        loc_id=222,
    ),
    "Valley.DuskApproach.West": ChestData(
        game_name="start.north-03-3",
        area="Koro Valley North",
        rule=HasAll("Low tide"),
        loc_id=223,
    ),
    "Valley.CliffSide": ChestData(
        game_name="start.east-01-1",
        area="Koro Valley",
        loc_id=224,
    ),
    "Valley.MedianDivide.Middle": ChestData(
        game_name="start.east-02-1",
        area="Koro Valley",
        loc_id=225,
    ),
    "Valley.MedianDivide.West": ChestData(
        game_name="start.east-02-2",
        area="Koro Valley",
        rule=HasAll("Kama", "Blunt"),
        loc_id=226,
    ),
    # TODO Maybe use an event for quickwood quest / repair these bridges (or area)
    "Valley.RedForest.West": ChestData(
        game_name="start.south-01-1",
        area="Koro Valley",
        rule=HasAll("Blunt", "Kama", "Valley bridges") & Has("Lyhamn level", count=1),
        loc_id=227,
    ),
    "Valley.RedForest.South": ChestData(
        game_name="start.south-01-2",
        area="Koro Valley",
        rule=HasAll("Blunt", "Range", "Valley bridges") & Has("Lyhamn level", count=1),
        loc_id=228,
    ),
    "Valley.Lake.West": ChestData(
        game_name="start.west-01-1",
        area="Koro Valley",
        # Requires starting Free the Fish quest
        rule=HasAll("Range", "Aether", "Blunt") & Has("Lyhamn level", count=1),
        loc_id=229,
    ),
    "Valley.Lake.North": ChestData(
        game_name="start.west-01-2",
        area="Koro Valley",
        # Requires starting Free the Fish quest
        rule=HasAll("Range", "Aether", "Blunt") & Has("Lyhamn level", count=1),
        loc_id=230,
    ),
    "Valley.SilverFileds.North": ChestData(
        game_name="start.peak-01-1",
        area="Silver Peak",
        rule=HasAll("Range"),
        loc_id=231,
    ),
    "Valley.HollowIncline.West": ChestData(
        game_name="start.peak-02-1",
        area="Silver Peak",
        rule=Has("Chakram"),
        loc_id=232,
    ),
    "Valley.HollowIncline.Middle": ChestData(
        game_name="start.peak-02-2",
        area="Silver Peak",
        rule=Has("Chakram"),
        loc_id=233,
    ),
    "Valley.Peak.East": ChestData(
        game_name="start.peak-03-1",
        area="Silver Peak",
        rule=Has("Chakram"),
        loc_id=234,
    ),
    "Valley.Peak.West": ChestData(
        game_name="start.peak-03-2",
        area="Silver Peak",
        rule=Has("Chakram"),
        loc_id=235,
    ),
    "Valley.RemisRock.West": ChestData(
        game_name="start.dng-outer-1",
        area="Trial of Aether Outside",
        rule=Has("Range"),
        loc_id=236,
    ),
    "Valley.RemisRock.North": ChestData(
        game_name="start.dng-outer-2",
        area="Aurum Plains",
        rule=HasAll("Aether", "Combat"),
        loc_id=237,
    ),
    "Valley.RemisRock.East": ChestData(
        game_name="start.dng-outer-3",
        area="Trial of Aether Outside",
        rule=HasAll("Range", "Blunt", "Aether"),
        loc_id=238,
    ),
    "Valley.RemisRock.NorthEast": ChestData(
        game_name="start.dng-outer-4",
        area="Trial of Aether Outside",
        rule=HasAll("Range", "Blunt", "Aether"),
        loc_id=239,
    ),
    "Lyhamn.Center.West": ChestData(
        game_name="start.village-01-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=240,
    ),
    # TODO probably remove this one, it is reachable with parkour but intended is likely CL2
    #"Lyhamn.Center.North": ChestData(
    #    game_name="start.village-01-2",
    #    area="Lyhamn",
    #    loc_id=241,
    #),
    "Lyhamn.Reef": ChestData(
        game_name="start.village-02-2-fix",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=242,
    ),
    "Lyhamn.Garden.East": ChestData(
        game_name="start.village-03-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=243,
    ),
    "Lyhamn.Garden.West": ChestData(
        game_name="start.village-03-2",
        area="Lyhamn",
        loc_id=244,
    ),
    "Lyhamn.PentersonOffering": ChestData(
        game_name="start.village-center01-giftChest1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=245,
    ),
    "Lyhamn.PetrosOffering": ChestData(
        game_name="start.village-center02-giftChest3",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=246,
    ),
    #"Lyhamn.Offering": ChestData(  # Not reachable ?
    #    game_name="start.village-center03-giftChest2",
    #    area="Lyhamn",
    #    rule=Has("Lyhamn level", count=1),
    #    loc_id=247,
    #),
    "Lyhamn.MarmisOffering": ChestData(
        game_name="start.village-center06-giftChest4",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=248,
    ),
    "Lyhamn.AlezandaOffering": ChestData(
        game_name="start.village-beach01-giftChest5",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=249,
    ),
    "Lyhamn.OrlandaOffering": ChestData(
        game_name="start.village-beach02-giftChest6",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
        loc_id=250,
    ),
    "EternalSpring.A3": ChestData(
        game_name="start.spring-trial-room-02-1",
        area="Eternal Spring",  # The rules are already considered in the area logic
        loc_id=251,
    ),
    "EternalSpring.A5": ChestData(
        game_name="start.spring-trial-room-03-1",
        area="Eternal Spring",
        rule=has_any_elements(2) & Has("Pierce Range"),
        loc_id=252,
    ),
    "EternalSpring.A6": ChestData(
        game_name="start.spring-trial-room-04-1",
        area="Eternal Spring",
        rule=has_any_elements(2) & Has("Pierce Range"),
        loc_id=253,
    ),
    "Lyhamn.ReefCave": ChestData(
        game_name="start.beach-spring-cave-01-1",
        area="Hotspring Cave",
        loc_id=254,
    ),
    "Lyhamn.FoggyLair": ChestData(
        game_name="start.beach-spring-cave-02-1",
        area="Hotspring Cave",
        rule=HasAll("Chakram", "Aether"),
        loc_id=255,
    ),
    "Aether.A1": ChestData(
        game_name="start.start-dng.f1-room-01-1",
        area="Trial of Aether A",
        rule=Has("Range"),
        loc_id=300,
    ),
    "Aether.A2.West": ChestData(
        game_name="start.start-dng.f1-room-02-1",
        area="Trial of Aether A",
        # Pierce not strictly required with parkour
        rule=HasAll("Pierce Range", "Filia", "Range") & Has("Aether Trial Mark", count=2),
        loc_id=301,
    ),
    "Aether.B4": ChestData(
        game_name="start.start-dng.f2-room-02b-1",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce Range", "Aether") & Has("Aether Trial Mark", count=2),
        loc_id=302,
    ),
    "Aether.A4": ChestData(
        game_name="start.start-dng.f1-room-04-1",
        area="Trial of Aether A",
        rule=HasAll("Blunt", "Filia", "Range") & Has("Aether Trial Mark", count=2),
        loc_id=303,
    ),
    "Aether.B7": ChestData(
        game_name="start.start-dng.f1-room-04b",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce Range", "Aether"),
        loc_id=304,
    ),
    "Aether.A2.East": ChestData(
        game_name="start.start-dng.f1-room-02-key",
        area="Trial of Aether A",
        # The grounded switch can be activated from melee, or from range with another element
        rule=HasAll("Range", "Filia") & (Has("Melee") | has_any_elements(2)),
        loc_id=305,
    ),
    "Aether.B5": ChestData(
        game_name="start.start-dng.f2-room-03-key",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce Range", "Aether"),
        loc_id=306,
    ),
    "ScalaMoor.Sodden.North": ChestData(
        game_name="swamp.center-02-1",
        area="Swamp.Entrance",
        rule=Has("Kama"),
        loc_id=400,
    ),
    "ScalaMoor.Sodden.Center": ChestData(
        game_name="swamp.center-02-2",
        area="Swamp.Entrance",
        rule=Has("Kama"),
        loc_id=401,
    ),
    "ScalaMoor.Pollo.East": ChestData(
        game_name="swamp.center-09-1",
        area="Swamp.Entrance",
        loc_id=402,
    ),
    "ScalaMoor.Pollo.West": ChestData(
        game_name="swamp.center-09-3",
        area="Swamp.PastMired",
        rule=Has("Kama"),
        loc_id=403,
    ),
    # This requires weaving things a bit everywhere, the rules also account for reaching all those areas
    "ScalaMoor.Pollo.North": ChestData(
        game_name="swamp.center-09-2",
        area="Swamp.North",
        rule=HasAll("Kama", "Cryo", "Physis", "Filia"),
        loc_id=404,
    ),
    "ScalaMoor.DeepBog.West": ChestData(
        game_name="swamp.center-03-1",
        area="Swamp.CowBoss",
        rule=HasAll("Kama", "Filia"),
        loc_id=405,
    ),
    # Past Mired
    "ScalaMoor.Mired.West": ChestData(
        game_name="swamp.center-04-1",
        area="Swamp.PastMired",
        rule=HasAll("Kama", "Filia"),
        loc_id=406
    ),
    "ScalaMoor.Training.South": ChestData(
        game_name="swamp.center-05-1",
        area="Swamp.PastMired",
        loc_id=407,
    ),
    "ScalaMoor.Mired.NorthWest": ChestData(
        game_name="swamp.center-04-2",
        area="Swamp.PastMired",
        loc_id=408,
    ),
    "ScalaMoor.Creek.NorthWest": ChestData(
        game_name="swamp.center-06-1",
        area="Swamp.North",
        loc_id=409,
    ),
    "ScalaMoor.Sunken.North": ChestData(
        game_name="swamp.center-08-1",
        area="Swamp.North",
        rule=Has("Kama") & has_any_elements(2),
        loc_id=410,
    ),
    "ScalaMoor.Stepped.North": ChestData(
        game_name="swamp.center-07-1",
        area="Swamp.North",
        rule=Has("Kama"),
        loc_id=411,
    ),
    "ScalaMoor.Thicket.West": ChestData(
        game_name="swamp.center-10-1",
        area="Swamp.Fulcrum",
        loc_id=412,
    ),
    "ScalaMoor.Thicket.Puzzle": ChestData(
        game_name="swamp.one-puzzle-dng",
        area="Swamp.Fulcrum",
        rule=Has("Kama") & has_any_elements(2),
        loc_id=413,
    ),
    # TODO Check for Combat Pierce everywhere
    "Cryo.A3": ChestData(
        game_name="swamp.swamp-dng.room-a3-key",
        area="Cryo.Entrance",
        rule=HasAll("Kama", "Range", "Filia"),
        loc_id=450,
    ),
    "Cryo.A4.South": ChestData(
        game_name="swamp.swamp-dng.room-a4-1",
        area="Cryo.1Door",
        rule=HasAll("Range"),
        loc_id=451,
    ),
    "Cryo.A2": ChestData(
        game_name="swamp.swamp-dng.room-a4-1",
        area="Cryo.1Door",
        rule=HasAll("Kama", "Filia") & has_any_elements(2),
        loc_id=452,
    ),
    "Cryo.C1.Center": ChestData(
        game_name="swamp.swamp-dng.room-c1-2",
        area="Cryo.C",
        rule=HasAll("Kama", "Chakram", "Cryo", "Aether"),
        loc_id=453,
    ),
    "Cryo.C1.North": ChestData(
        game_name="swamp.swamp-dng.room-c1-1",
        area="Cryo.C",
        rule=HasAll("Kama", "Chakram", "Cryo", "Aether"),
        loc_id=454,
    ),
    "Cryo.Lake.East": ChestData(
        game_name="swamp.swamp-dng.room-center-key",
        area="Cryo.C",
        rule=HasAll("Kama", "Chakram", "Cryo", "Aether"),
        loc_id=455,
    ),
    "Cryo.D3": ChestData(
        game_name="swamp.swamp-dng.room-d3",
        area="Cryo.D",
        rule=HasAll("Kama", "Cryo", "Pierce Combat"),  # TODO Require buttons + big combat
        loc_id=456,
    ),
    "Cryo.A4.West": ChestData(
        game_name="swamp.swamp-dng.room-a4-2",
        area="Cryo.D",
        rule=HasAll("Kama", "Cryo", "Physis", "Aether", "Filia"),
        loc_id=457,
    ),
    "Cryo.D1": ChestData(
        game_name="swamp.swamp-dng.room-d1-key",
        area="Cryo.D",
        rule=HasAll("Kama", "Cryo", "Shuriken") & has_any_elements(2),
        loc_id=458,
    ),
    "Cryo.E2": ChestData(
        game_name="swamp.swamp-dng.room-e2-key",
        area="Cryo.E",
        rule=HasAll("Cryo", "Physis", "Range", "Filia"),
        loc_id=459,
    ),
}
