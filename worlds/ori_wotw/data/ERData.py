from enum import IntEnum

class Groups(IntEnum):
    # Main room
    MAIN = 0
    OW_1O_2 = 1
    MOKI_HUT = 2
    OW_3 = 3
    # Non dead-ends
    WILLOW = 4
    IW_1 = 5  # First floor of Inner Wellspring
    # Dead-ends
    WOODS_HUT = 6
    IW_2 = 7
    DEAD = 8

group_lookup: dict[str, Groups] = {
    "GladesTown.TwillenHome (Door)": Groups.MAIN,
    "GladesTown.KeyMokiHutInside (Door)": Groups.DEAD,
    "GladesTown.MotayHutDoor (Door)": Groups.MAIN,
    "GladesTown.MotayHutInside (Door)": Groups.DEAD,
    "GladesTown.UpperWest (Door)": Groups.MAIN,
    "GladesTown.InsideThirdHut (Door)": Groups.DEAD,
    "GladesTown.AcornMoki (Door)": Groups.MAIN,
    "GladesTown.AcornCave (Door)": Groups.DEAD,
    "GladesTown.AboveOpher (Door)": Groups.MAIN,
    "GladesTown.StorageHut (Door)": Groups.DEAD,
    "GladesTown.LupoHouse (Door)": Groups.MAIN,
    "GladesTown.InsideLupoHouse (Door)": Groups.DEAD,
    "GladesTown.HoleHutEntrance (Door)": Groups.MAIN,
    "GladesTown.InsideHoleHut (Door)": Groups.DEAD,
    "OuterWellspring.EntranceDoor (Door)": Groups.MAIN,
    "OuterWellspring.WestDoor (Door)": Groups.OW_1O_2,
    "OuterWellspring.EastDoor (Door)": Groups.OW_1O_2,
    "OuterWellspring.TopDoor (Door)": Groups.OW_3,
    "InnerWellspring.EntranceDoor (Door)": Groups.IW_1,
    "InnerWellspring.WestDoor (Door)": Groups.IW_1,
    "InnerWellspring.EastDoor (Door)": Groups.IW_2,
    "InnerWellspring.Teleporter (Door)": Groups.DEAD,
    "WoodsEntry.FamilyHut (Door)": Groups.MAIN,
    "WoodsEntry.FamilyHutInside (Door)": Groups.WOODS_HUT,
    "UpperReach.TreeRoom (Door)": Groups.MAIN,
    "UpperReach.SeedHut (Door)": Groups.DEAD,
    "UpperWastes.OutsideRuins (Door)": Groups.MAIN,
    "WindtornRuins.UpperRuinsDoor (Door)": Groups.DEAD,
    "WeepingRidge.WillowEntranceLedge (Door)": Groups.MAIN,
    "WillowsEnd.Entry (Door)": Groups.WILLOW,
    "WillowsEnd.Upper (Door)": Groups.WILLOW,
    "WillowsEnd.ShriekArena (Door)": Groups.DEAD
}

target_lookup: dict[Groups, list[Groups]] = {
    # A Group cannot connect to itself
    ### Main rooms (groups 0 to 3) cannot connect to each other
    # No special rules for these
    Groups.MAIN: [Groups.WILLOW, Groups.IW_1, Groups.WOODS_HUT, Groups.IW_2, Groups.DEAD],
    # Don't connect the doors opened by the lever in Inner Wellspring 1 to this room
    Groups.OW_1O_2: [Groups.WILLOW, Groups.WOODS_HUT, Groups.IW_2, Groups.DEAD],
    # Don't connect the Key Moki Hut to the Doll location in the woods hut (as it is required to enter)
    Groups.MOKI_HUT: [Groups.WILLOW, Groups.IW_1, Groups.IW_2, Groups.DEAD],
    # Entering the 3rd room in Wellspring requires removing the corruption from Inner Wellspring 2
    Groups.OW_3: [Groups.WILLOW, Groups.IW_1, Groups.WOODS_HUT, Groups.DEAD],
    ### Other rooms that are not dead ends (groups 4, 5)
    # No special rule for Willow
    Groups.WILLOW: [Groups.MAIN, Groups.OW_1O_2, Groups.MOKI_HUT, Groups.OW_3, Groups.IW_1, Groups.WOODS_HUT,
                    Groups.IW_2, Groups.DEAD],
    # No connection with the OW_1O_2 doors
    Groups.IW_1: [Groups.MAIN, Groups.MOKI_HUT, Groups.OW_3, Groups.WILLOW, Groups.WOODS_HUT, Groups.IW_2, Groups.DEAD],
    ### Dead ends: don't connect these to themselves to not lock the generator (groups 6 to 8)
    # No connection with the Key Moki hut
    Groups.WOODS_HUT: [Groups.MAIN, Groups.OW_1O_2, Groups.OW_3, Groups.WILLOW, Groups.IW_1],
    # No connection with the top door of Outer Wellspring
    Groups.IW_2: [Groups.MAIN, Groups.OW_1O_2, Groups.MOKI_HUT, Groups.WILLOW, Groups.IW_1],
    # No special rules for these
    Groups.DEAD: [Groups.MAIN, Groups.OW_1O_2, Groups.MOKI_HUT, Groups.OW_3, Groups.WILLOW, Groups.IW_1],
}
