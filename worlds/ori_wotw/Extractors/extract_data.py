"""
Extracts the data on events (or states), regions (or anchors), and locations (or pickups).

The data is extracted from an `areas.wotw` file and a `loc_data.csv` file.
"""

import re
import os


com = re.compile(" *#")  # Detects comments
sp = re.compile("^ *")  # Used for indents
col = re.compile(" .*:")  # name between space and colon
tra = re.compile(" *$")  # Trailing space
sep = re.compile(" at ")


def extract_all(override=False):
    """Extracts the data on events, regions and locations."""
    extract_events(override)
    extract_quests(override)
    extract_regions(override)


def extract_quests(override=False):
    """Extracts the data and writes a file with the quest table."""
    if os.path.exists("./Quests.py"):
        if override:
            print("Warning: File replaced")
        else:
            raise FileExistsError("The file `Quests.py` already exists. Use `override=True` to override it.")

    header = ("\"\"\"\n"
              "File generated with `extract_data.py` by running `extract_quests()` on an `areas.wotw` file.\n\n"
              "You can find such a file at https://github.com/ori-community/wotw-seedgen/tree/main/wotw_seedgen .\n\n"
              "Do not edit manually.\n"
              "\"\"\"\n\n\n")

    quests = []

    quest_txt = header + "quest_table = [\n"

    with open("./areas.wotw", "r") as file:
        temp = file.readlines()

    for p in temp:
        m = com.search(p)  # Removes the comments
        if m:
            p = p[:m.start()]
        m = tra.search(p)  # Removes the trailing spaces
        if m:
            p = p[:m.start()]
        if p == "":
            continue

        m = sp.match(p)  # Counts the indents
        if m is None:
            ind = 0
        else:
            ind = (m.end()+1)//2

        if ind == 1:
            if "pickup" in p or "quest" in p:
                name = col.search(p[2:]).group()[1:-1]
                if "quest" in p and name not in quests:
                    quests.append(name)

    for quest in quests:
        quest_txt += f"    \"{quest}\",\n"
    quest_txt = quest_txt[:-2]
    quest_txt += "\n    ]\n"

    with open("Quests.py", "w") as file:
        file.write(quest_txt)
        print("The file Quests.py has been successfully created.")


def extract_events(override=False):
    """Extracts the data and writes them as a table with the events."""
    if os.path.exists("./Events.py"):
        if override:
            print("Warning: File replaced")
        else:
            raise FileExistsError("The file `Events.py` already exists. Use `override=True` to override it.")

    header = ("\"\"\"\n"
              "File generated with `extract_data.py` by running `extract_events()` on an `areas.wotw` file.\n\n"
              "You can find such a file at https://github.com/ori-community/wotw-seedgen/tree/main/wotw_seedgen .\n\n"
              "Do not edit manually.\n"
              "\"\"\"\n\n")

    glitch_events = ["WaveDash", "HammerJump", "SwordJump", "GlideHammerJump"]
    combat_events = ["Combat.Ranged", "Combat.Aerial", "Combat.Dangerous", "Combat.Shielded", "Combat.Bat",
                     "Combat.Sand"]
    other_events = ["BreakCrystal"]
    events = glitch_events + combat_events + other_events

    event_txt = "event_table = [\n"

    with open("./areas.wotw", "r") as file:
        temp = file.readlines()

    for p in temp:
        m = com.search(p)  # Removes the comments
        if m:
            p = p[:m.start()]
        m = tra.search(p)  # Removes the trailing spaces
        if m:
            p = p[:m.start()]
        if p == "":
            continue

        m = sp.match(p)  # Counts the indents
        if m is None:
            ind = 0
        else:
            ind = (m.end()+1)//2

        if ind == 0:
            if "requirement" in p:
                name = col.search(p).group()[1:-1]
                if name not in events:
                    events.append(name)
        elif ind == 1:
            if "state" in p:
                name = col.search(p[2:]).group()[1:-1]
                if name not in events:
                    events.append(name)

    for event in events:
        event_txt += f"    \"{event}\",\n"

    event_txt = event_txt[:-2]
    event_txt += "\n    ]\n"

    with open("Events.py", "w") as file:
        file.write(header + event_txt)
        print("The file Events.py has been successfully created.")


def extract_regions(override=False):
    """Extracts the data and writes a file with the regions."""
    if os.path.exists("./Regions.py"):
        if override:
            print("Warning: File replaced")
        else:
            raise FileExistsError("The file `Regions.py` already exists. Use `override=True` to override it.")

    header = ("\"\"\"\n"
              "File generated with `extract_data.py` by running `extract_regions()` on an `areas.wotw` file.\n\n"
              "You can find such a file at https://github.com/ori-community/wotw-seedgen/tree/main/wotw_seedgen .\n\n"
              "Do not edit manually.\n"
              "\"\"\"\n\n\n")

    regions = []

    with open("./areas.wotw", "r") as file:
        temp = file.readlines()

    for p in temp:
        m = com.search(p)  # Removes the comments
        if m:
            p = p[:m.start()]
        m = tra.search(p)  # Removes the trailing spaces
        if m:
            p = p[:m.start()]
        if p == "":
            continue

        m = sp.match(p)  # Counts the indents
        if m is None:
            ind = 0
        else:
            ind = (m.end()+1)//2

        if ind == 0:
            if "anchor" in p:
                name = col.search(p).group()[1:-1]
                s = sep.search(name)
                if s:
                    anc = name[:s.start()]
                else:
                    anc = name
                if anc not in regions:
                    regions.append(anc)

    region_txt = header + "region_table = [\n"

    for region in regions:
        region_txt += f"    \"{region}\",\n"

    region_txt = region_txt[:-2]
    region_txt += "\n    ]\n"

    with open("Regions.py", "w") as file:
        file.write(region_txt)
        print("The file Regions.py has been successfully created.")
