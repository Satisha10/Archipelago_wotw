from rule_builder.rules import Has, HasAll

from .data_structures import ChestData


# TODO see if these chests are reachable in 0.1, and write logic rules
# TODO Names

# TODO other locations: quests rewards to show (randomize them ?)

chests: dict[str, ChestData] = {
    "TODO": ChestData(
        game_name="hub.west-01-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.south-01-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.south-03-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.south-03-2",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.south-03-3",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.south-04-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.south-04-2",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.south-04-3",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.north-01-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.north-01-2",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "TODO": ChestData(
        game_name="hub.north-01-3",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.north-02-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.north-04-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.north-05-1",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "TODO": ChestData(
        game_name="hub.center-06-1",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "TODO": ChestData(
        game_name="hub.center-06-2",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.center-06-3",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="hub.town-south-1",
        area="Sundalan",
    ),
    "TODO": ChestData(
        game_name="hub.bridge-01-1",
        area="Aurum Plains",
    ),
    "TODO": ChestData(
        game_name="start.center-01-1",
        area="Koro Valley",
        rule=Has("Aether"),
    ),
    "TODO": ChestData(
        game_name="start.center-01-2",
        area="Koro Valley",
        rule=Has("Aether"),
    ),
    "TODO": ChestData(
        game_name="start.center-01-3",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-02-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-02-2",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO": ChestData(
        game_name="start.center-02-3",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-03-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-04-1",
        area="Koro Valley",
        rule=Has("Hammer"),
    ),
    "TODO": ChestData(
        game_name="start.center-04-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-04-3",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO": ChestData(
        game_name="start.center-05-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-05-2",
        area="Koro Valley",
        rule=HasAll("Filia", "Aether"),
    ),
    "TODO": ChestData(
        game_name="start.center-06-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-06-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-06-3",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.center-07-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO": ChestData(
        game_name="start.center-07-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(  # TODO not sure this one is reachable yet
        game_name="start.center-08-1",
        area="Koro Valley",
        rule=HasAll("Aether", "Fulcrum Mark"),
    ),
    "TODO": ChestData(  # TODO Item name
        game_name="start.north-01-2",
        area="Koro Valley",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.north-02-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.north-02-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.north-03-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO": ChestData(
        game_name="start.north-03-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.north-03-3",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.east-01-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.east-02-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.east-02-2",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO": ChestData(
        game_name="start.south-01-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO": ChestData(
        game_name="start.south-01-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.west-01-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.west-01-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.peak-01-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.peak-02-1",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO": ChestData(
        game_name="start.peak-02-2",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO": ChestData(
        game_name="start.peak-03-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.peak-03-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.dng-outer-1",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.dng-outer-2",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.dng-outer-3",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.dng-outer-4",
        area="Koro Valley",
    ),
    "TODO": ChestData(
        game_name="start.village-01-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-01-2",
        area="Lyhamn",
    ),
    "TODO": ChestData(
        game_name="start.village-02-2-fix",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-03-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-03-2",
        area="Lyhamn",
    ),
    "TODO": ChestData(
        game_name="start.village-center01-giftChest1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-center02-giftChest3",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-center03-giftChest2",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-center06-giftChest4",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-beach01-giftChest5",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.village-beach02-giftChest6",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO": ChestData(
        game_name="start.spring-trial-room-02-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.spring-trial-room-03-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.spring-trial-room-04-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.beach-spring-cave-01-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.beach-spring-cave-02-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(  # TODO Key logic
        game_name="start.start-dng.f1-room-01-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.start-dng.f1-room-02-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.start-dng.f2-room-02b-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.start-dng.f1-room-04-1",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.start-dng.f1-room-04b",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.start-dng.f1-room-02-key",
        area="Trial of Aether",
    ),
    "TODO": ChestData(
        game_name="start.start-dng.f2-room-03-key",
        area="Trial of Aether",
    ),
}
