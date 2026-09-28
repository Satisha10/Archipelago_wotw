import json
import os

from .header import header_py, header_ts

from ..quests import quests
from ..chests import chests
from ..dishes import dishes
from ..story_locations import story_loc


class LocationData:
    """Class that contain the extracted data."""
    def __init__(self):
        self.location_name_to_id: dict[str, int] = {}
        self.location_gamename_to_id: dict[str, int] = {}
        self.used_ids: dict[int, str] = {}
    def add_data(self, loc_dict: dict):
        """
        Method to add the locations from a data file to the class data.

        :param loc_dict: dict of str to a class with `game_name` and `loc_id` attributes, which has the data.
        """
        for name, data in loc_dict.items():
            if name in self.location_name_to_id:
                raise ValueError(f"Duplicate location name `{name}`")
            if data.loc_id in self.used_ids:
                raise ValueError(f"Duplicate item id `{data.loc_id}` between `{name}` "
                                 f"and `{self.used_ids[data.loc_id]}`")
            self.location_name_to_id.setdefault(name, data.loc_id)
            self.location_gamename_to_id.setdefault(data.game_name, data.loc_id)
            self.used_ids.setdefault(data.loc_id, name)

loc_data = LocationData()

loc_data.add_data(story_loc)
loc_data.add_data(chests)
loc_data.add_data(dishes)
loc_data.add_data(quests)

def loc_name_id():
    """Generate the location name to ID dict for the AP World."""
    base_path = "output_apworld/locations.py"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_py("location_id_map.py", "loc_name_id"))
        f.write("location_name_to_id: dict[str, int] = {\n")
        for name, loc_id in loc_data.location_name_to_id.items():
            f.write(f'    "{name}": {loc_id},\n')
        f.write("}\n")

    print(f"File {base_path} created.")


# TODO use a loop instead of json
def loc_gamename_id():
    """Generate the location game-name to ID map for the client."""
    base_path = "output_client/location_gamename_id.ts"
    file_path = os.path.join("worlds/alabaster_dawn/data_extractors", base_path)
    with open(file_path, "w") as f:
        f.write(header_ts("location_id_map.py", "loc_gamename_id"))
        f.write("export const loc_game_name_id = new Map<string, number>([\n    [")
        temp = json.dumps(loc_data.location_gamename_to_id)[1:-1]
        output = temp.replace(", ", "],\n    [")
        output = output.replace(":", ",")
        f.write(output)
        f.write("]\n]);\n")
    print(f"File {base_path} created.")
