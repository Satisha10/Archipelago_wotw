from rule_builder.rules import True_, Has, HasAll

from .data_structures import AreaData

areas: dict[str, AreaData] = {
    "Lyhamn": AreaData(
        connections={
            "Koro Valley": True_(),
        },
    ),
    "Koro Valley": AreaData(
        connections={
            "Lyhamn": True_(),
            "Trial of Aether": HasAll("Filia", "Low tide"),
            "Aurum Plains": Has("Boat"),
        },
    ),
    "Trial of Aether": AreaData(
        connections={
            "Koro Valley": Has("Low tide"),
            "Aurum Plains": True_(),
        },
    ),
    "Aurum Plains": AreaData(
        connections={
            "Lyhamn": Has("Boat"),
            "Trial of Aether": Has("Filia"),
            "Sundalan": True_(),
        },
    ),
    "Sundalan": AreaData(
        connections={
            "Lyhamn": True_(),
        },
    ),
}
