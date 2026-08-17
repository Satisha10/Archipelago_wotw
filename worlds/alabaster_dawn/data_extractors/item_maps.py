import os

from BaseClasses import ItemClassification

from .header import header_ts, header_py

from ..data_structures import ItemData

from ..item_data.main_items import main_items
from ..item_data.major_gems import major_gems
from ..item_data.minor_gems import minor_gems
from ..item_data.gem_recipies import gem_recipies
from ..item_data.dish_recipies import dishes
from ..item_data.divine_arts import arts
from ..item_data.essences import essences

class ItemMap:
    """Class that contain the item data that will be added to the generated code."""
    def __init__(self):
        self.data: dict[str, ItemData] = {}
        self.groups: dict[str, list[str]] = {"Filler": []}
        self.id = 1

    def add_items(self, mapping: dict[str, ItemData]):
        """Add the items from mapping into the data."""
        for name, item in mapping.items():
            if name in self.data:
                raise ValueError(f"Duplicate item name `{name}`")
            self.data.setdefault(
                name,
                ItemData(
                    item.classification,
                    item.pool_quantity,
                    item.item_quantity,
                    item.game_name,
                    item.item_type,
                    self.id,
                )
            )
            self.id += 1

            if item.item_type not in self.groups:
                self.groups.setdefault(item.item_type, [])
            self.groups[item.item_type].append(name)
            if item.classification == ItemClassification.filler:
                self.groups["Filler"].append(name)


item_map = ItemMap()

item_map.add_items(main_items)
item_map.add_items(arts)
item_map.add_items(major_gems)
item_map.add_items(minor_gems)
item_map.add_items(gem_recipies)
item_map.add_items(dishes)
item_map.add_items(essences)


type_def = """type ItemData = {
    name: string;
    qty: number;
}
"""

def item_gamename_map():
    """Generate a map between item name and the game-name + quantity for the client."""
    base_path = "output_client/item_name_gamedata.ts"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_ts("item_maps.py", "item_gamename_map"))
        f.write(type_def)
        f.write("\nexport const item_name_data = new Map<string, ItemData>([\n")

        for name, data in item_map.data.items():
            data_txt = "{" + f'name: "{data.game_name}", qty: {data.item_quantity}' + "}"
            f.write(f'    ["{name}", {data_txt}],\n')

        f.write("]);\n")
    print(f"File {base_path} created.")


def item_data_ap():
    """Generate the item name to data (ID, classification, quantity) for the AP World."""
    base_path = "output_apworld/items.py"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_py("item_maps.py", "item_data_ap"))
        f.write("from BaseClasses import ItemClassification as IC\n\n")
        f.write("from .data_structures import APItem\n\n")
        f.write("items: dict[str, APItem] = {\n")
        for name, item in item_map.data.items():
            f.write(f'    "{name}": APItem(id={item.id}, quantity={item.pool_quantity}, '
                    f'classification=IC({item.classification})),\n')
        f.write("}\n")

    print(f"File {base_path} created.")


def item_groups_ap():
    """Generate the item groups for the AP World."""
    base_path = "output_apworld/item_groups.py"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_py("item_maps.py", "item_groups_ap"))
        f.write("item_groups: dict[str, list[str]] = {\n")
        for group, items in item_map.groups.items():
            f.write(f'    "{group}": [\n')
            for item in items:
                f.write(f'        "{item}",\n')
            f.write("    ],\n")
        f.write("}\n")

    print(f"File {base_path} created.")
