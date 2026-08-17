"""
Entry file for the file extractor, for AP World and client files.
The required files are located in the AP World.
The client files are written in ./output_client, and the AP World files to ./output_apworld.

Use `python -m worlds.alabaster_dawn.data_extractors` in the console to run this.
"""

import argparse

from worlds.alabaster_dawn.data_extractors.location_id_map import loc_gamename_id, loc_name_id
from worlds.alabaster_dawn.data_extractors.item_maps import item_gamename_map, item_data_ap, item_groups_ap

parser = argparse.ArgumentParser(
    prog="Data extractor for Alabaster Dawn AP",
    description="Generate python and typescript files for the AP World and client using data from the AP World."
)

parser.add_argument(
    "-c", "--no_client",
    dest="no_client",
    action=argparse.BooleanOptionalAction,
    help="Don't generate client files (in typescript)."
)

parser.add_argument(
    "-a", "--no_apworld",
    dest="no_ap",
    action=argparse.BooleanOptionalAction,
    help="Don't generate AP World files (in python)."
)

arguments = parser.parse_args()

if not arguments.no_client:
    loc_gamename_id()
    item_gamename_map()

if not arguments.no_ap:
    loc_name_id()
    item_data_ap()
    item_groups_ap()
