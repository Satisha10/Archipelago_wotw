from rule_builder.rules import True_, Has, HasAll

from .data_structures import AreaData


areas: dict[str, AreaData] = {
    "Lyhamn": AreaData(
        connections={
            "Koro Valley": True_(),
            "Hotspring Cave": Has("Lyhamn level", count=1),
        },
    ),
    "Koro Valley": AreaData(
        connections={
            "Lyhamn": True_(),
            # Eternal spring can be entered with just the key, but you need the rest to be able to do anything useful.
            "Eternal Spring": Has("Fulcrum Mark", count=3) & HasAll("Filia", "Aether", "Blunt", "Pierce", "Chakram"),
            "Silver Peak": Has("Blunt"),
            "Koro Valley North": Has("Valley bridges")
        },
    ),
    "Koro Valley North": AreaData(  # Dusk approach and ValleyEntrance
        connections={
            "Trial of Aether A": HasAll("Filia", "Low tide"),
            "Aurum Plains": Has("Boat travel"),
            "Koro Valley": True_(),
        },
    ),
    "Silver Peak": AreaData(
        connections={
            "Koro Valley": Has("Blunt"),
        }
    ),
    "Hotspring Cave": AreaData(  # Cave for Spring's Return quest
        connections={
            "Lyhamn": True_(),
        }
    ),
    "Trial of Aether A": AreaData(
        connections={
            "Trial of Aether Outside": HasAll("Filia", "Aether", "Blunt") & Has("Aether Trial Mark", count=2)
        },
    ),
    "Trial of Aether Outside": AreaData(  # Between A and B, up until the divine bridge
        connections={
            "Aurum Plains": HasAll("Aether", "Filia", "Chakram"),
        }
    ),
    "Trial of Aether B": AreaData(
        connections={
            # No connection to Outside, since it is before the divine bridge, that is activated when coming from Trial A
            "Aurum Plains": True_(),
        }
    ),
    "Eternal Spring": AreaData(
        connections={
            "Koro Valley": Has("Fulcrum Mark", count=3),
        },
    ),
    "Aurum Plains": AreaData(
        connections={
            "Koro Valley North": Has("Boat travel"),
            "Trial of Aether B": HasAll("Combat", "Aether"),
            "Sundalan": True_(),
            "Swamp.Entrance": Has("Kama"),  # TODO Separate with Somu
        },
    ),
    "Sundalan": AreaData(
        connections={
            "Aurum Plains": True_(),
        },
    ),
    # Entrance, before the Moss cow fight
    "Swamp.Entrance": AreaData(
        connections={
            "Aurum Plains": True_(),
            "Swamp.DeepBog": HasAll("Kama", "Physis"),
        },
    ),
    # After the Moss cow fight, before the bridge in Mired Crossing
    "Swamp.DeepBog": AreaData(
        connections={
            "Swamp.Entrance": HasAll("Kama", "Physis"),
            "Swamp.PastMired": HasAll("Kama", "Filia"),
            "Swamp.Fulcrum": Has("Fulcrum Mark", count=3),
        },
    ),
    # After the bridge in Mired Crossing, up until the bridge in Muddy Creek
    "Swamp.PastMired": AreaData(
        connections={
            "Swamp.Entrance": True_(),  # Through Pollo's Abode
            "Swamp.North": Has("Kama"),
        },
    ),
    # After the bridge in Muddy Creek
    "Swamp.North": AreaData(
        connections={
            "Swamp.PastMired": Has("Kama"),
            "Cryo.Entrance": True_(),
            "Swamp.Entrance": True_(),
        },
    ),
    # After the door
    "Swamp.Fulcrum": AreaData(
        connections={
            "Swamp.DeepBog": Has("Fulcrum Mark", count=3),
        },
    ),
    # Dungeon entrance, before 1st door
    "Cryo.Entrance": AreaData(
        connections={
            "Cryo.1Door": Has("Kama") & Has("Cryo Trial Mark", count=1),
        },
    ),
    # After the 1st door, until going in the C rooms (so after Cryo + mini boss)
    "Cryo.1Door": AreaData(
        connections={
            "Cryo.C": HasAll("Range", "Filia", "Cryo", "Slash Combat"),
        },
    ),
    "Cryo.C": AreaData(
        connections={
            "Cryo.D": Has("Cryo Trial Mark", count=2) & Has("Slash Combat"),
        },
    ),
    "Cryo.D": AreaData(
        connections={
            "Cryo.E": Has("Cryo Trial Mark", count=3) & Has("Combat"),  # TODO See if combat requires smthg else
        },
    ),
    "Cryo.E": AreaData(
        connections={
        },
    ),
}
