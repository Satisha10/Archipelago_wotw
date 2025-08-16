"""
Generated file, do not edit manually.

See https://github.com/Satisha10/APworld_wotw_extractors for the code.
Generated with `extract_rules.py`.
"""


doors_vanilla: list[tuple[str, str]] = [ # Vanilla door connections
    ('Door.GladesTown.TwillenHome', 'Door.GladesTown.KeyMokiHutInside'),
    ('Door.GladesTown.KeyMokiHutInside', 'Door.GladesTown.TwillenHome'),
    ('Door.GladesTown.MotayHut', 'Door.GladesTown.MotayHutInside'),
    ('Door.GladesTown.MotayHutInside', 'Door.GladesTown.MotayHut'),
    ('Door.GladesTown.UpperWest', 'Door.GladesTown.InsideThirdHut'),
    ('Door.GladesTown.InsideThirdHut', 'Door.GladesTown.UpperWest'),
    ('Door.GladesTown.AcornMoki', 'Door.GladesTown.AcornCave'),
    ('Door.GladesTown.AcornCave', 'Door.GladesTown.AcornMoki'),
    ('Door.GladesTown.AboveOpher', 'Door.GladesTown.StorageHut'),
    ('Door.GladesTown.StorageHut', 'Door.GladesTown.AboveOpher'),
    ('Door.GladesTown.LupoHouse', 'Door.GladesTown.InsideLupoHouse'),
    ('Door.GladesTown.InsideLupoHouse', 'Door.GladesTown.LupoHouse'),
    ('Door.GladesTown.HoleHutEntrance', 'Door.GladesTown.InsideHoleHut'),
    ('Door.GladesTown.InsideHoleHut', 'Door.GladesTown.HoleHutEntrance'),
    ('Door.OuterWellspring.EntranceDoor', 'Door.InnerWellspring.EntranceDoor'),
    ('Door.OuterWellspring.WestDoor', 'Door.InnerWellspring.WestDoor'),
    ('Door.OuterWellspring.EastDoor', 'Door.InnerWellspring.EastDoor'),
    ('Door.OuterWellspring.TopDoor', 'Door.InnerWellspring.Teleporter'),
    ('Door.InnerWellspring.EntranceDoor', 'Door.OuterWellspring.EntranceDoor'),
    ('Door.InnerWellspring.WestDoor', 'Door.OuterWellspring.WestDoor'),
    ('Door.InnerWellspring.EastDoor', 'Door.OuterWellspring.EastDoor'),
    ('Door.InnerWellspring.Teleporter', 'Door.OuterWellspring.TopDoor'),
    ('Door.WoodsEntry.FamilyHut', 'Door.WoodsEntry.FamilyHutInside'),
    ('Door.WoodsEntry.FamilyHutInside', 'Door.WoodsEntry.FamilyHut'),
    ('Door.UpperReach.TreeRoom', 'Door.UpperReach.SeedHut'),
    ('Door.UpperReach.SeedHut', 'Door.UpperReach.TreeRoom'),
    ('Door.UpperWastes.OutsideRuins', 'Door.WindtornRuins.UpperRuinsDoor'),
    ('Door.WindtornRuins.UpperRuinsDoor', 'Door.UpperWastes.OutsideRuins'),
    ('Door.WeepingRidge.WillowEntranceLedge', 'Door.WillowsEnd.Entry'),
    ('Door.WillowsEnd.Entry', 'Door.WeepingRidge.WillowEntranceLedge'),
    ('Door.WillowsEnd.Upper', 'Door.WillowsEnd.ShriekArena'),
    ('Door.WillowsEnd.ShriekArena', 'Door.WillowsEnd.Upper')
    ]

doors_map: dict[str, int] = {  # Mapping to door ID
    "Door.GladesTown.TwillenHome": 9,
    "Door.GladesTown.KeyMokiHutInside": 10,
    "Door.GladesTown.MotayHut": 5,
    "Door.GladesTown.MotayHutInside": 6,
    "Door.GladesTown.UpperWest": 3,
    "Door.GladesTown.InsideThirdHut": 4,
    "Door.GladesTown.AcornMoki": 13,
    "Door.GladesTown.AcornCave": 14,
    "Door.GladesTown.AboveOpher": 11,
    "Door.GladesTown.StorageHut": 12,
    "Door.GladesTown.LupoHouse": 1,
    "Door.GladesTown.InsideLupoHouse": 2,
    "Door.GladesTown.HoleHutEntrance": 7,
    "Door.GladesTown.InsideHoleHut": 8,
    "Door.OuterWellspring.EntranceDoor": 15,
    "Door.OuterWellspring.WestDoor": 17,
    "Door.OuterWellspring.EastDoor": 19,
    "Door.OuterWellspring.TopDoor": 21,
    "Door.InnerWellspring.EntranceDoor": 16,
    "Door.InnerWellspring.WestDoor": 18,
    "Door.InnerWellspring.EastDoor": 20,
    "Door.InnerWellspring.Teleporter": 22,
    "Door.WoodsEntry.FamilyHut": 25,
    "Door.WoodsEntry.FamilyHutInside": 26,
    "Door.UpperReach.TreeRoom": 23,
    "Door.UpperReach.SeedHut": 24,
    "Door.UpperWastes.OutsideRuins": 27,
    "Door.WindtornRuins.UpperRuinsDoor": 28,
    "Door.WeepingRidge.WillowEntranceLedge": 29,
    "Door.WillowsEnd.Entry": 30,
    "Door.WillowsEnd.Upper": 31,
    "Door.WillowsEnd.ShriekArena": 32
    }

