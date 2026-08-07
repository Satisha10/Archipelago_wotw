import json
import os

from .header import header_py, header_ts

from ..quests import quests
from ..chests import chests
from ..dishes import dishes

location_name_to_id: dict[str, int] = {}
location_gamename_to_id: dict[str, int] = {}

i = 0

for chest, chest_data in chests.items():
    location_name_to_id.setdefault(chest, i)
    location_gamename_to_id.setdefault(chest_data.game_name, i)
    i += 1

for quest, quest_data in quests.items():
    location_name_to_id.setdefault(quest, i)
    location_gamename_to_id.setdefault(quest_data.game_name, i)
    i += 1

for dish, dish_data in dishes.items():
    location_name_to_id.setdefault(dish, i)
    location_gamename_to_id.setdefault(dish_data.game_name, i)
    i += 1

def loc_name_id():
    """Generate the location name to ID dict for the AP World."""
    base_path = "output_apworld/locations.py"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_py("location_id_map.py", "loc_name_id"))
        f.write("location_name_to_id = {}\n".format(location_name_to_id))
    print(f"File {base_path} created.")

def loc_gamename_id():  # TODO Format properly, add the variable name, and add the missing semicolons
    """Generate the location game name to ID mapping for the client."""
    base_path = "output_client/location_gamename_id.ts"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_ts("location_gamename_id.ts", "loc_gamename_id"))
        f.write(json.dumps(location_gamename_to_id))
    print(f"File {base_path} created.")
