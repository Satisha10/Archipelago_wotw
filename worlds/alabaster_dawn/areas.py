from rule_builder.rules import True_, Has, HasAll

from .data_structures import AreaData


areas: dict[str, AreaData] = {
    "Lyhamn": AreaData(
        connections={
            "Koro Valley": True_(),
            "Hotspring Cave": True_(),  # TODO
        },
    ),
    "Koro Valley": AreaData(
        connections={
            "Lyhamn": True_(),
            "Trial of Aether": HasAll("Filia", "Low tide"),
            "Aurum Plains": Has("Boat"),
            # Eternal spring can be entered with just the key, but you need the rest to be able to do anything useful.
            "Eternal Spring": Has("Fulcrum Mark", count=2) & HasAll("Filia", "Aether", "Blunt", "Pierce", "Chakram"),
            "Silver Peak": Has("Blunt"),
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
            "Koro Valley": Has("Low tide"),
            "Trial of Aether Outside": HasAll("Filia", "Aether")  # TODO
        },
    ),
    "Trial of Aether Outside": AreaData(  # Between A and B, up until the divine bridge
        connections={
            "Trial of Aether A": True_(),  # TODO verify
            # Trial of Aether B is tied to Aurum Plains
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
            "Lyhamn": Has("Boat"),
            "Trial of Aether B": True_(),  # TODO fight before the entrance, maybe need that too
            "Sundalan": True_(),
        },
    ),
    "Sundalan": AreaData(
        connections={
            "Aurum Plains": True_(),
        },
    ),
}
