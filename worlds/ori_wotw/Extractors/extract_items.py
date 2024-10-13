"""Extracts the list of items and locations in Ori and the Will of the Wisps."""

import os
prefix = "101111110010101001"
# base_id = int(prefix + "0000000000000000000000000000000000", 2)


def extract_items(override=False):
    """Extracts the data and writes a file with the item table and the item groups."""
    if os.path.exists("./Items.py"):
        if override:
            print("Warning: File replaced")
        else:
            raise FileExistsError("The file `Items.py` already exists. Use `override=True` to override it.")

    global prefix
    store = []  # Stores the IDs to check for duplicates

    header = ("\"\"\"\n"
              "File generated with `extract_items.py` with the `Items_data.csv` file.\n\n"
              "Do not edit manually.\n"
              "\"\"\"\n\n"
              "from BaseClasses import ItemClassification\n\n")

    with open("./Items_data.csv", "r") as file:
        temp = file.readlines()

    item_txt = header + "item_table = {  # The tuple contains the amount, the classification, the ID\n"

    for line in temp[1:]:
        data = line.split(",")
        item_id = compute_id(prefix, data[3], data[4], data[5])
        if item_id in store:
            raise ValueError(f"{item_id} duplicated.\n"
                             f"Group = {data[4]}, State = {data[5]},  Item = {data[0]}")
        store.append(item_id)
        item_txt += f"    \"{data[0]}\": ({int(data[1])}, ItemClassification.{data[2]}, {item_id}),\n"
    item_txt = item_txt[:-2]
    item_txt += "\n    }\n\n\n"

    item_txt += ('group_table = {\n'
                 '    "skills": ["Sword", "DoubleJump", "Regenerate", "Bow", "Dash", "Bash", "Grapple", "Glide", "Flap", "Grenade",\n'
                 '               "Flash", "WaterDash", "Burrow", "Launch", "Water", "WaterBreath", "Hammer", "Sentry", "Shuriken",\n'
                 '               "Spear", "Blaze"],\n'
                 '    "collectibles": ["Health", "Energy", "Keystone", "Ore", "ShardSlot", "AncestralLight_1", "AncestralLight_2"],\n'
                 '    "spirit_light": ["1 SpiritLight", "50 SpiritLight", "100 SpiritLight", "200 SpiritLight"],\n'
                 '    "shards": ["Overcharge", "TripleJump", "Wingclip", "Bounty", "Swap", "Magnet", "Splinter", "Reckless", "Quickshot",\n'
                 '               "Resilience", "LightHarvest", "Vitality", "LifeHarvest", "EnergyHarvest", "EnergyShard", "LifePact",\n'
                 '               "LastStand", "Sense", "UltraBash", "UltraGrapple", "Overflow", "Thorn", "Catalyst", "Turmoil", "Sticky",\n'
                 '               "Finesse", "SpiritSurge", "Lifeforce", "Deflector", "Fracture", "Arcing"],\n'
                 '    "teleporters": ["BurrowsTP", "DenTP", "EastPoolsTP", "DepthsTP", "WellspringTP", "ReachTP", "HollowTP",\n'
                 '                    "WestWoodsTP", "EastWoodsTP", "WestWastesTP", "EastWastesTP", "OuterRuinsTP", "WillowTP",\n'
                 '                    "MarshTP", "GladesTP"],\n'
                 '    "extratp": ["WestPoolsTP", "InnerRuinsTP"],\n'
                 '    "weapon_upgrades": ["ExplodingSpear", "HammerShockwave", "StaticShuriken", "ChargeBlaze", "RapidSentry"],\n'
                 '    "bonus": ["HealthRegeneration", "EnergyRegeneration", "ExtraDoubleJump", "ExtraAirDash", "BlazeEfficiency",\n'
                 '              "SpearEfficiency", "ShurikenEfficiency", "SentryEfficiency", "BowEfficiency", "RegenerateEfficiency",\n'
                 '              "FlashEfficiency", "GrenadeEfficiency"],\n'
                 '    "bonus+": ["RapidSword", "RapidHammer", "RapidSpear", "QuickshotUpgrade", "MeltingBow",\n'
                 '               "MeltingBlaze", "MeltingSword", "MeltingHammer", "MeltingSpear", "MeltingShuriken", "UnchargedBashnades",\n'
                 '               "ExtraGrenade", "SplinterGrenade", "UnlimitedSentries", "SentryFireRate", "BashableShuriken"],\n'
                 '    "skillup": ["Jumpgrade", "SkillVelocity"]\n'
                 '    }\n')

    with open("Items.py", "w") as file:
        file.write(item_txt)
        print("The file Items.py has been successfully created.")


def extract_locs(override=False):
    """Extracts the data and writes a file with the location table."""
    if os.path.exists("./Locations.py"):
        if override:
            print("Warning: File replaced")
        else:
            raise FileExistsError("The file `Locations.py` already exists. Use `override=True` to override it.")

    global prefix
    store = []  # Stores the IDs to check for duplicates

    header = ("\"\"\"\n"
              "File generated with `extract_items.py` with the `loc_data.csv` file.\n\n"
              "Do not edit manually.\n"
              "\"\"\"\n\n\n")

    with open("./loc_data.csv", "r") as file:
        temp = file.readlines()

    loc_txt = header + "loc_table = {\n"

    for line in temp[1:]:
        data = line.split(", ")
        loc_id = compute_id(prefix, "location", data[5], data[7], data[8])
        if loc_id in store:
            raise ValueError(f"{loc_id} duplicated.\n"
                             f"Group = {data[5]}, State = {data[7]}, Value = {data[8]}, Location = {data[0]}")
        store.append(loc_id)
        loc_txt += f"    \"{data[0]}\": {loc_id},\n"
    loc_txt = loc_txt[:-2]
    loc_txt += "\n    }\n"

    with open("Locations.py", "w") as file:
        file.write(loc_txt)
        print("The file Locations.py has been successfully created.")


def compute_id(pre, item_type, group, state, value=""):
    """Returns the item ID according to its type, and its uberstate group and value."""  # TODO: link ref for how to compute ID
    assert int(group) <= 65535, f"group must be smaller than 65535 (is equal to {group})"
    assert int(state) <= 65535, f"state must be smaller than 65535 (is equal to {state})"
    if value:
        assert int(value) <= 255, f"state must be smaller than 255 (is equal to {value})"

    if item_type == "location":
        b_item_type = "00"
        if not value:
            value = "0"
    elif item_type == "item":
        b_item_type = "01"
        value = ""
    elif item_type == "resource":
        b_item_type = "10"
        value = ""
    else:
        raise ValueError(f"{item_type} is not a valid type of item (must be location, item or resource).")

    b_group = bin(int(group))[2:]
    if item_type == "location":
        b_group = "0" * (8-len(b_group[-8:])) + b_group[-8:]
    else:
        b_group = "0" * (16-len(b_group)) + b_group

    b_state = bin(int(state))[2:]
    b_state = "0" * (16-len(b_state)) + b_state

    if value:
        b_value = bin(int(value))[2:]
        b_value = "0" * (8-len(b_value)) + b_value
    else:
        b_value = ""

    total = pre + b_item_type + b_group + b_state + b_value
    return int(total, 2)
