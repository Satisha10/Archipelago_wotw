import os
from dataclasses import dataclass

from .header import header_ts

from ..items import items

@dataclass
class OutData:
    game_name: str
    item_quantity: int


item_map: dict[str, OutData] = {}

for item, item_data in items.items():
    item_map.setdefault(item, OutData(item_data.game_name, item_data.item_quantity))

type_def = """type ItemData = {
    name: string;
    qty: number;
}
"""

# TODO Map name to [game_name, quantity] for items
def item_gamename_map():
    """Generate a map between item name and the game-name + quantity for the client."""
    base_path = "output_client/item_name_gamedata.ts"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_ts("item_maps.py", "item_gamename_map"))
        f.write(type_def)
        f.write("\nexport const item_name_data = new Map<string, ItemData>([\n")

        for name, data in item_map.items():
            data_txt = "{" + f'name: "{data.game_name}", qty: {data.item_quantity}' + "}"
            f.write(f'    ["{name}", {data_txt}],\n')

        f.write("]);\n")
    print(f"File {base_path} created.")
