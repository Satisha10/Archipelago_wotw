from rule_builder.rules import Has, HasAll

from .data_structures import ChestData


# TODO see if these chests are reachable in 0.1, and write logic rules
# TODO Names

# TODO other locations: quests rewards to show (randomize them ?)

chests: dict[str, ChestData] = {
    "TODO1": ChestData(
        game_name="hub.west-01-1",
        area="Aurum Plains",
    ),
    "TODO2": ChestData(
        game_name="hub.south-01-1",
        area="Aurum Plains",
    ),
    "TODO3": ChestData(
        game_name="hub.south-03-1",
        area="Aurum Plains",
    ),
    "TODO4": ChestData(
        game_name="hub.south-03-2",
        area="Aurum Plains",
    ),
    "TODO5": ChestData(
        game_name="hub.south-03-3",
        area="Aurum Plains",
    ),
    "TODO6": ChestData(
        game_name="hub.south-04-1",
        area="Aurum Plains",
    ),
    "TODO7": ChestData(
        game_name="hub.south-04-2",
        area="Aurum Plains",
    ),
    "TODO8": ChestData(
        game_name="hub.south-04-3",
        area="Aurum Plains",
    ),
    "TODO9": ChestData(
        game_name="hub.north-01-1",
        area="Aurum Plains",
    ),
    "TODO10": ChestData(
        game_name="hub.north-01-2",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "TODO11": ChestData(
        game_name="hub.north-01-3",
        area="Aurum Plains",
    ),
    "TODO12": ChestData(
        game_name="hub.north-02-1",
        area="Aurum Plains",
    ),
    "TODO13": ChestData(
        game_name="hub.north-04-1",
        area="Aurum Plains",
    ),
    "TODO14": ChestData(
        game_name="hub.north-05-1",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "TODO15": ChestData(
        game_name="hub.center-06-1",
        area="Aurum Plains",
        rule=Has("Kama"),
    ),
    "TODO16": ChestData(
        game_name="hub.center-06-2",
        area="Aurum Plains",
    ),
    "TODO17": ChestData(
        game_name="hub.center-06-3",
        area="Aurum Plains",
    ),
    "TODO18": ChestData(
        game_name="hub.town-south-1",
        area="Sundalan",
    ),
    "TODO19": ChestData(
        game_name="hub.bridge-01-1",
        area="Aurum Plains",
    ),
    "TODO20": ChestData(
        game_name="start.center-01-1",
        area="Koro Valley",
        rule=Has("Aether"),
    ),
    "TODO21": ChestData(
        game_name="start.center-01-2",
        area="Koro Valley",
        rule=Has("Aether"),
    ),
    "TODO22": ChestData(
        game_name="start.center-01-3",
        area="Koro Valley",
    ),
    "TODO23": ChestData(
        game_name="start.center-02-1",
        area="Koro Valley",
    ),
    "TODO24": ChestData(
        game_name="start.center-02-2",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO25": ChestData(
        game_name="start.center-02-3",
        area="Koro Valley",
    ),
    "TODO26": ChestData(
        game_name="start.center-03-2",
        area="Koro Valley",
    ),
    "TODO27": ChestData(
        game_name="start.center-04-1",
        area="Koro Valley",
        rule=Has("Hammer"),
    ),
    "TODO28": ChestData(
        game_name="start.center-04-2",
        area="Koro Valley",
    ),
    "TODO29": ChestData(
        game_name="start.center-04-3",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO30": ChestData(
        game_name="start.center-05-1",
        area="Koro Valley",
    ),
    "TODO31": ChestData(
        game_name="start.center-05-2",
        area="Koro Valley",
        rule=HasAll("Filia", "Aether"),
    ),
    "TODO32": ChestData(
        game_name="start.center-06-1",
        area="Koro Valley",
    ),
    "TODO33": ChestData(
        game_name="start.center-06-2",
        area="Koro Valley",
    ),
    "TODO34": ChestData(
        game_name="start.center-06-3",
        area="Koro Valley",
    ),
    "TODO35": ChestData(
        game_name="start.center-07-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO36": ChestData(
        game_name="start.center-07-2",
        area="Koro Valley",
    ),
    "TODO37": ChestData(  # TODO not sure this one is reachable yet
        game_name="start.center-08-1",
        area="Koro Valley",
        rule=Has("Aether") & Has("Fulcrum Mark", count=2),
    ),
    "TODO38": ChestData(
        game_name="start.north-01-2",
        area="Koro Valley",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO39": ChestData(
        game_name="start.north-02-1",
        area="Koro Valley",
    ),
    "TODO40": ChestData(
        game_name="start.north-02-2",
        area="Koro Valley",
    ),
    "TODO41": ChestData(
        game_name="start.north-03-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO42": ChestData(
        game_name="start.north-03-2",
        area="Koro Valley",
    ),
    "TODO43": ChestData(
        game_name="start.north-03-3",
        area="Koro Valley",
    ),
    "TODO44": ChestData(
        game_name="start.east-01-1",
        area="Koro Valley",
    ),
    "TODO45": ChestData(
        game_name="start.east-02-1",
        area="Koro Valley",
    ),
    "TODO46": ChestData(
        game_name="start.east-02-2",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO47": ChestData(
        game_name="start.south-01-1",
        area="Koro Valley",
        rule=Has("Kama"),
    ),
    "TODO48": ChestData(
        game_name="start.south-01-2",
        area="Koro Valley",
    ),
    "TODO49": ChestData(
        game_name="start.west-01-1",
        area="Koro Valley",
    ),
    "TODO50": ChestData(
        game_name="start.west-01-2",
        area="Koro Valley",
    ),
    "TODO51": ChestData(
        game_name="start.peak-01-1",
        area="Koro Valley",
    ),
    "TODO52": ChestData(
        game_name="start.peak-02-1",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO53": ChestData(
        game_name="start.peak-02-2",
        area="Koro Valley",
        rule=Has("Chakram"),
    ),
    "TODO54": ChestData(
        game_name="start.peak-03-1",
        area="Koro Valley",
    ),
    "TODO55": ChestData(
        game_name="start.peak-03-2",
        area="Koro Valley",
    ),
    "TODO56": ChestData(
        game_name="start.dng-outer-1",
        area="Koro Valley",
    ),
    "TODO57": ChestData(
        game_name="start.dng-outer-2",
        area="Koro Valley",
    ),
    "TODO58": ChestData(
        game_name="start.dng-outer-3",
        area="Koro Valley",
    ),
    "TODO59": ChestData(
        game_name="start.dng-outer-4",
        area="Koro Valley",
    ),
    "TODO60": ChestData(
        game_name="start.village-01-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO61": ChestData(
        game_name="start.village-01-2",
        area="Lyhamn",
    ),
    "TODO62": ChestData(
        game_name="start.village-02-2-fix",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO63": ChestData(
        game_name="start.village-03-1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO64": ChestData(
        game_name="start.village-03-2",
        area="Lyhamn",
    ),
    "TODO65": ChestData(
        game_name="start.village-center01-giftChest1",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO66": ChestData(
        game_name="start.village-center02-giftChest3",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO67": ChestData(
        game_name="start.village-center03-giftChest2",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO68": ChestData(
        game_name="start.village-center06-giftChest4",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO69": ChestData(
        game_name="start.village-beach01-giftChest5",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO70": ChestData(
        game_name="start.village-beach02-giftChest6",
        area="Lyhamn",
        rule=Has("Lyhamn level", count=1),
    ),
    "TODO71": ChestData(
        game_name="start.spring-trial-room-02-1",
        area="Eternal Spring",
    ),
    "TODO72": ChestData(
        game_name="start.spring-trial-room-03-1",
        area="Eternal Spring",
    ),
    "TODO73": ChestData(
        game_name="start.spring-trial-room-04-1",
        area="Eternal Spring",
    ),
    "TODO74": ChestData(
        game_name="start.beach-spring-cave-01-1",
        area="Eternal Spring",
    ),
    "TODO75": ChestData(
        game_name="start.beach-spring-cave-02-1",
        area="Eternal Spring",
    ),
    "TODO76": ChestData(  # TODO Key logic
        game_name="start.start-dng.f1-room-01-1",
        area="Trial of Aether",
    ),
    "TODO77": ChestData(
        game_name="start.start-dng.f1-room-02-1",
        area="Trial of Aether",
    ),
    "TODO78": ChestData(
        game_name="start.start-dng.f2-room-02b-1",
        area="Trial of Aether",
    ),
    "TODO79": ChestData(
        game_name="start.start-dng.f1-room-04-1",
        area="Trial of Aether",
    ),
    "TODO80": ChestData(
        game_name="start.start-dng.f1-room-04b",
        area="Trial of Aether",
    ),
    "TODO81": ChestData(
        game_name="start.start-dng.f1-room-02-key",
        area="Trial of Aether",
    ),
    "TODO82": ChestData(
        game_name="start.start-dng.f2-room-03-key",
        area="Trial of Aether",
    ),
}
