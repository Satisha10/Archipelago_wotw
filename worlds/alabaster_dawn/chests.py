from rule_builder.rules import Has, HasAll, AtLeast

from .data_structures import ChestData
from .rule_helpers import has_any_elements

# TODO for any_elements, check is aether or physis are explicitly required

chests: dict[str, ChestData] = {
    "Plains.Somu": ChestData(
        game_name="hub.west-01-1",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "Plains.Watchtower": ChestData(
        game_name="hub.south-01-1",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "Plains.HiddenSteep.West": ChestData(
        game_name="hub.south-03-1",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "Plains.HiddenSteep.SouthEast": ChestData(
        game_name="hub.south-03-2",
        area="Aurum Plains",
        rule=HasAll("Aether", "Chakram", "Filia"),
    ),
    "Plains.HiddenSteep.Hidden": ChestData(
        game_name="hub.south-03-3",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "Plains.RiverRoad.Statue": ChestData(
        game_name="hub.south-04-1",
        area="Aurum Plains",
    ),
    "Plains.RiverRoad.NorthEast": ChestData(
        game_name="hub.south-04-2",
        area="Aurum Plains",
        rule=HasAll("Filia", "Range"),
    ),
    "Plains.RiverRoad.North": ChestData(
        game_name="hub.south-04-3",
        area="Aurum Plains",
    ),
    "Plains.OldFarm.East": ChestData(
        game_name="hub.north-01-1",
        area="Aurum Plains",
        rule=Has("Range")
    ),
    "Plains.OldFarm.SouthWest": ChestData(
        game_name="hub.north-01-2",
        area="Aurum Plains",
    ),
    "Plains.OldFarm.Quest": ChestData(
        game_name="hub.north-01-3",
        area="Aurum Plains",
    ),
    "Plains.NorthBend.North": ChestData(
        game_name="hub.north-02-1",
        area="Aurum Plains",
        rule=HasAll("Blunt", "Combat"),
    ),
    #"Plains.ImpactCrater": ChestData(  # Nyx nest, not reachable ? (need to go on sundalan's walls)
    #    game_name="hub.north-04-1",
    #    area="Aurum Plains",
    #),
    "Plains.RuinedRanch.West": ChestData(
        game_name="hub.north-05-1",
        area="Aurum Plains",
        rule=HasAll("Kama", "Filia"), # Aether + slash for combat ?
    ),
    "Plains.SouthBend.West": ChestData(
        game_name="hub.center-06-1",
        area="Aurum Plains",
        rule=HasAll("Kama", "Filia", "Aether", "Chakram"),  # Need to solve the big puzzle before
    ),
    "Plains.SouthBend.East": ChestData(
        game_name="hub.center-06-2",
        area="Aurum Plains",
    ),
    "Plains.SouthBend.North": ChestData(
        game_name="hub.center-06-3",
        area="Aurum Plains",
        rule=Has("Range"),
    ),
    "Sundalan.Meridi": ChestData(
        game_name="hub.town-south-1",
        area="Sundalan",
    ),
    "Plains.SolGate": ChestData(
        game_name="hub.bridge-01-1",
        area="Aurum Plains",
    ),
    "Plains.SolGate.Puzzle": ChestData(
        game_name="hub.bridge-01-puzzle-01",
        area="Aurum Plains",
        rule=HasAll("Chakram", "Aether", "Filia") & Has("Fulcrum Mark", count=2) & has_any_elements(2),
    ),
    "Valley.ForkedRoad.East": ChestData(
        game_name="start.center-01-1",
        area="Koro Valley",
        rule=HasAll("Aether", "Range"),
    ),
    "Valley.ForkedRoad.West": ChestData(
        game_name="start.center-01-2",
        area="Koro Valley",
        rule=HasAll("Aether", "Range"),
    ),
    "Valley.ForkedRoad.South": ChestData(
        game_name="start.center-01-3",
        area="Koro Valley",
    ),
    "Valley.ReaversEnd.North": ChestData(
        game_name="start.center-02-1",
        area="Koro Valley",
    ),
    "Valley.ReaversEnd.East": ChestData(
        game_name="start.center-02-2",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "Valley.ReaversEnd.Boss": ChestData(  # TODO Requires hammer to go from upwards ? and bridge from down
        game_name="start.center-02-3",
        area="Koro Valley",
    ),
    "Valley.EyeRemis": ChestData(
        game_name="start.center-03-2",
        area="Koro Valley",
    ),
    "Valley.Kamu.West": ChestData(
        game_name="start.center-04-1",
        area="Koro Valley",
        rule=Has("Blunt"),
    ),
    "Valley.Kamu.NorthEast": ChestData(
        game_name="start.center-04-2",
        area="Koro Valley",
    ),
    "Valley.Kamu.South": ChestData(
        game_name="start.center-04-3",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "Valley.Fossil.South": ChestData(
        game_name="start.center-05-1",
        area="Koro Valley",
    ),
    "Valley.Fossil.East": ChestData(
        game_name="start.center-05-2",
        area="Koro Valley",
        rule=HasAll("Filia", "Aether", "Range"),
    ),
    "Valley.Lumber.EternalSpringChest": ChestData(
        game_name="start.center-06-1",
        area="Koro Valley",
    ),
    "Valley.Lumber.West": ChestData(
        game_name="start.center-06-2",
        area="Koro Valley",
    ),
    "Valley.Lumber.East": ChestData(
        game_name="start.center-06-3",
        area="Koro Valley",
        rule=Has("Range"),
    ),
    "Valley.LyhamnShelter.East": ChestData(
        game_name="start.center-07-1",
        area="Koro Valley",
        rule=HasAll("Kama", "Pierce"),
    ),
    "Valley.LyhamnShelter.Combat": ChestData(
        game_name="start.center-07-2",
        area="Koro Valley",
    ),
    "EternalSpring.Outside": ChestData(
        game_name="start.center-08-1",
        area="Eternal Spring",
        rule=has_any_elements(2),  # TODO check that it is only reachable once dng complete
    ),
    "Valley.Crescent.SouthWest": ChestData(
        game_name="start.north-01-2",
        area="Koro Valley",
        rule=Has("Lyhamn level", count=1),
    ),
    "Valley.ValleyEntrance.Bridge": ChestData(
        game_name="start.north-02-1",
        area="Koro Valley",
    ),
    "Valley.ValleyEntrance.East": ChestData(
        game_name="start.north-02-2",
        area="Koro Valley",
        rule=Has("Range"),
    ),
    "Valley.DuskApproach.East": ChestData(
        game_name="start.north-03-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "Valley.DuskApproach.South": ChestData(  # Missable in 0.1.0, but might be ok if tide is an item
        game_name="start.north-03-2",
        area="Koro Valley",
    ),
    "Valley.DuskApproach.West": ChestData(  # TODO Hammer because of scripted fight ? Also tide + maybe bridge
        game_name="start.north-03-3",
        area="Koro Valley",
    ),
    "Valley.CliffSide": ChestData(
        game_name="start.east-01-1",
        area="Koro Valley",
    ),
    "Valley.MedianDivide.Middle": ChestData(
        game_name="start.east-02-1",
        area="Koro Valley",
    ),
    "Valley.MedianDivide.West": ChestData(
        game_name="start.east-02-2",
        area="Koro Valley",
        rule=HasAll("Kama", "Blunt"),
    ),
    "Valley.RedForest.West": ChestData(
        game_name="start.south-01-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "Valley.RedForest.South": ChestData(
        game_name="start.south-01-2",
        area="Koro Valley",  # Might require CL2 or blunt
    ),
    "Valley.Lake.West": ChestData(
        game_name="start.west-01-1",
        area="Koro Valley",
        rule=HasAll("Range", "Aether"),  # Also need the quest: CL1 ?
    ),
    "Valley.Lake.North": ChestData(
        game_name="start.west-01-2",
        area="Koro Valley",
        rule=HasAll("Range", "Aether", "Blunt"),
    ),
    # TODO do an area for peak because of hammer barrier ?
    "Valley.SilverFileds.North": ChestData(
        game_name="start.peak-01-1",
        area="Silver Peak",
        rule=HasAll("Range"),
    ),
    "Valley.HollowIncline.West": ChestData(
        game_name="start.peak-02-1",
        area="Silver Peak",
        rule=Has("Chakram"),
    ),
    "Valley.HollowIncline.Middle": ChestData(
        game_name="start.peak-02-2",
        area="Silver Peak",
        rule=Has("Chakram"),
    ),
    "Valley.Peak.East": ChestData(
        game_name="start.peak-03-1",
        area="Silver Peak",
        rule=Has("Chakram"),
    ),
    "Valley.Peak.West": ChestData(
        game_name="start.peak-03-2",
        area="Silver Peak",
        rule=Has("Chakram"),
    ),
    "Valley.RemisRock.West": ChestData(
        game_name="start.dng-outer-1",
        area="Trial of Aether Outside",
        rule=Has("Range")
    ),
    "Valley.RemisRock.North": ChestData(
        game_name="start.dng-outer-2",
        area="Aurum Plains",
        rule=HasAll("Aether", "Combat")
    ),
    "Valley.RemisRock.East": ChestData(
        game_name="start.dng-outer-3",
        area="Trial of Aether Outside",
        rule=HasAll("Range", "Blunt", "Aether"),
    ),
    "Valley.RemisRock.NorthEast": ChestData(
        game_name="start.dng-outer-4",
        area="Trial of Aether Outside",
        rule=HasAll("Range", "Blunt", "Aether"),
    ),
    "Lyhamn.Center.West": ChestData(
        game_name="start.village-01-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "Lyhamn.Center.North": ChestData(
        game_name="start.village-01-2",
        area="Lyhamn",
    ),
    "Lyhamn.Reef": ChestData(
        game_name="start.village-02-2-fix",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "Lyhamn.Garden.East": ChestData(
        game_name="start.village-03-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "Lyhamn.Garden.West": ChestData(
        game_name="start.village-03-2",
        area="Lyhamn",
    ),
    "Lyhamn.PentersonOffering": ChestData(
        game_name="start.village-center01-giftChest1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "Lyhamn.PetrosOffering": ChestData(
        game_name="start.village-center02-giftChest3",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    #"Lyhamn.Offering": ChestData(  # Not reachable ?
    #    game_name="start.village-center03-giftChest2",
    #    area="Lyhamn",
    #    rule=Has("Lyhamn level", count=1),
    #),
    "Lyhamn.MarmisOffering": ChestData(
        game_name="start.village-center06-giftChest4",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "Lyhamn.AlezandaOffering": ChestData(
        game_name="start.village-beach01-giftChest5",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "Lyhamn.OrlandaOffering": ChestData(
        game_name="start.village-beach02-giftChest6",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "EternalSpring.A3": ChestData(
        game_name="start.spring-trial-room-02-1",
        area="Eternal Spring",  # The rules are already considered in the area logic
    ),
    "EternalSpring.A5": ChestData(
        game_name="start.spring-trial-room-03-1",
        area="Eternal Spring",
        rule=has_any_elements(2),  # TODO Also need a range pierce, make range TYPE a thing
    ),
    "EternalSpring.A6": ChestData(
        game_name="start.spring-trial-room-04-1",
        area="Eternal Spring",
        rule=has_any_elements(2),
    ),
    "Lyhamn.ReefCave": ChestData(
        game_name="start.beach-spring-cave-01-1",
        area="Hotspring Cave",
    ),
    "Lyhamn.FoggyLair": ChestData(
        game_name="start.beach-spring-cave-02-1",
        area="Hotspring Cave",
        rule=Has("Chakram"),
    ),
    "Aether.A1": ChestData(
        game_name="start.start-dng.f1-room-01-1",
        area="Trial of Aether A",
        rule=Has("Range")
    ),
    "Aether.A2.West": ChestData(
        game_name="start.start-dng.f1-room-02-1",
        area="Trial of Aether A",
        rule=HasAll("Pierce", "Filia", "Key", "Range")
    ),
    "Aether.B4": ChestData(
        game_name="start.start-dng.f2-room-02b-1",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce", "Aether"),
    ),
    "Aether.A2.NorthEast": ChestData(
        game_name="start.start-dng.f1-room-04-1",
        area="Trial of Aether A",
        rule=HasAll("Blunt", "Filia", "Key", "Range")
    ),
    "Aether.B7": ChestData(
        game_name="start.start-dng.f1-room-04b",
        area="Trial of Aether B",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce", "Aether")
    ),# TODO key for a2 to a5 + loc for aether element
    "Aether.A2.East": ChestData(
        game_name="start.start-dng.f1-room-02-key",
        area="Trial of Aether A",
        # The grounded switch can be activated from melee, or from range with another element
        rule=HasAll("Range", "Melee", "Filia") & (Has("Melee") | has_any_elements(2))
    ),
    "Aether.B5": ChestData(
        game_name="start.start-dng.f2-room-03-key",
        area="Trial of Aether",
        rule=HasAll("Filia", "Chakram", "Blunt", "Pierce", "Aether")
    ),
    # TODO Nyx Spire, which also requires 2nd element
}
