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
            "Eternal Spring": Has("Fulcrum Mark", count=2) & HasAll("Filia", "Aether", "Blunt", "Pierce", "Chakram"),
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
            "Koro Valley North": Has("Low tide"),  # TODO maybe not true if you arrived from top
            "Trial of Aether Outside": HasAll("Filia", "Aether") & Has("Trial Mark", count=2)  # TODO
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
            "Koro Valley": Has("Fulcrum Mark", count=2),
        },
    ),
    "Aurum Plains": AreaData(
        connections={
            "Koro Valley North": Has("Boat travel"),
            "Trial of Aether B": HasAll("Combat", "Aether"),
            "Sundalan": True_(),
        },
    ),
    "Sundalan": AreaData(
        connections={
            "Aurum Plains": True_(),
        },
    ),
}
