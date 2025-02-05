from typing import List, Dict

loc_sets: Dict[str, List[str]] = {
    "Quests": [
        "MarshSpawn.TokkKeystoneQuest",
        "MarshSpawn.MokkFangQuest",
        "MarshSpawn.TokkTabletQuest",
        "EastHollow.KwolokAmuletQuest",
        "OuterWellspring.TheLostCompass",
        "WoodsEntry.LastTreeBranch",
        "WoodsEntry.TreeSeed",
        "EastPools.KwolokAmuletQI",
        "LowerWastes.EerieGemQI",
        "GladesTown.TwillenGemQuest",
        "GladesTown.FamilyReunionKey",
        "GladesTown.MokiAcornQuest",
        "EastHollow.HandToHandMap",
        "GladesTown.HandToHandPouch",
        "InnerWellspring.HandToHandHerbs",
        "LowerReach.HandToHandSoup",
        "LowerReach.HandToHandHat",
        "GladesTown.HandToHandLantern",
        "LowerDepths.HandToHandSilk",
        "EastPools.HandToHandSpyglass",
        "GladesTown.HandToHandCanteen",
        "LowerWastes.HandToHandMapstone",
        "WindtornRuins.HandToHandComplete",
    ],
    "ExtraQuests": [
        "MarshSpawn.CaveKS",
        "MarshSpawn.FangQI",
        "HowlsDen.SwordTree",
        "MidnightBurrows.TabletQI",
        "EastHollow.ForestsVoice",
        "GladesTown.AcornQI",
        "InnerWellspring.NeedleQI",
        "InnerWellspring.BlueMoonSeed",
        "InnerWellspring.WaterEscape",
        "WoodsEntry.DollQI",
        "LowerReach.ForestsMemory",
        "UpperReach.SpringSeed",
        "UpperDepths.LightcatcherSeed",
        "UpperDepths.ForestsEyes",
        "EastPools.GrassSeed",
        "WestPools.ForestsStrength",
        "UpperWastes.FlowersSeed",
        "WindtornRuins.Seir",
    ],
    "Rebuild": [
        "GladesTown.RebuildTheGlades",
        "GladesTown.RegrowTheGlades",
    ],
    "Trials": [
        "MarshPastOpher.SpiritTrial",
        "WestHollow.SpiritTrial",
        "OuterWellspring.SpiritTrial",
        "EastPools.SpiritTrial",
        "WoodsMain.SpiritTrial",
        "LowerReach.SpiritTrial",
        "LowerDepths.SpiritTrial",
        "LowerWastes.SpiritTrial",
    ],
    "Base": [
        "MarshSpawn.RockHC",
        "MarshSpawn.FirstPickupEX",
        "MarshSpawn.GrappleHC",
        "MarshSpawn.BridgeEX",
        "MarshSpawn.ResilienceShard",
        "MarshSpawn.ResilienceOre",
        "MarshSpawn.BashEC",
        "MarshSpawn.PreLupoEX",
        "MarshSpawn.LupoMap",
        "MarshSpawn.RegenTree",
        "MarshSpawn.LeverEC",
        "MarshSpawn.LeftTokkEX",
        "MarshSpawn.FightRoomEX",
        "MarshSpawn.CaveOre",
        "MarshSpawn.LongSwimEX",
        "MarshSpawn.BurrowOre",
        "MarshSpawn.LifepactShard",
        "MarshSpawn.BurrowsApproachLedgeEX",
        "MarshSpawn.CrusherSwimEX",
        "MarshSpawn.RecklessShard",
        "MarshSpawn.MokkEX",
        "MarshSpawn.FangEC",
        "MarshSpawn.DamageTree",
        "MarshSpawn.PoolsPathEX",
        "MidnightBurrows.LeftKS",
        "MidnightBurrows.RightKS",
        "MidnightBurrows.UpperKS",
        "MidnightBurrows.LowerKS",
        "MidnightBurrows.LupoMap",
        "MidnightBurrows.DeflectorShard",
        "HowlsDen.RightHC",
        "HowlsDen.LeftHC",
        "HowlsDen.AboveDoorKS",
        "HowlsDen.MagnetShard",
        "HowlsDen.BoneOre",
        "HowlsDen.AboveTPEX",
        "HowlsDen.LaserKS",
        "HowlsDen.CombatShrine",
        "HowlsDen.DoubleJumpEX",
        "HowlsDen.StickyShard",
        "HowlsDen.DoubleJumpTree",
        "MarshPastOpher.TrialLeftEX",
        "MarshPastOpher.TrialOre",
        "MarshPastOpher.TrialEC",
        "MarshPastOpher.TrialHC",
        "MarshPastOpher.TrialRightEX",
        "MarshPastOpher.CombatShrine",
        "MarshPastOpher.SwingPoleEX",
        "MarshPastOpher.LeftEyestone",
        "MarshPastOpher.RightEyestone",
        "MarshPastOpher.BowEC",
        "MarshPastOpher.BowTree",
        "MarshPastOpher.CeilingEX",
        "MarshPastOpher.PoolsPathEC",
        "MarshPastOpher.PoolsPathEX",
        "WestHollow.CrusherHC",
        "WestHollow.FarLeftEX",
        "WestHollow.RockPuzzleEX",
        "WestHollow.HiddenEC",
        "WestHollow.QuickshotShard",
        "WestHollow.SwimEC",
        "WestHollow.LupoMap",
        "WestHollow.TrialHC",
        "WestHollow.BelowLupoEX",
        "WestHollow.AboveDashEX",
        "WestHollow.DashRightEX",
        "WestHollow.CrusherEX",
        "WestHollow.DashTree",
        "EastHollow.GladesApproachOre",
        "EastHollow.HornBeetleFightEX",
        "EastHollow.SpikeLanternEX",
        "EastHollow.SecretRoofEX",
        "EastHollow.MortarEX",
        "EastHollow.BashEC",
        "EastHollow.BashHC",
        "EastHollow.BashEX",
        "EastHollow.BashTree",
        "EastHollow.RightKwolokEX",
        "EastHollow.SilentSwimEC",
        "EastHollow.SplinterShard",
        "EastHollow.KwolokSwimOre",
        "EastHollow.KwolokSwimLeftEX",
        "EastHollow.KwolokSwimRightEX",
        "EastHollow.DepthsExteriorEX",
        "GladesTown.HoleHutEC",
        "GladesTown.AboveGromHC",
        "GladesTown.LupoSwimHC",
        "GladesTown.UpperOre",
        "GladesTown.LowerOre",
        "GladesTown.ArcingShard",
        "GladesTown.BountyShard",
        "GladesTown.LupoSoupEX",
        "GladesTown.BraveMokiHutEX",
        "GladesTown.MotayHutEX",
        "GladesTown.HoleHutEX",
        "GladesTown.UpperLeftEX",
        "GladesTown.LupoSwimMiddleEX",
        "GladesTown.CaveBurrowEX",
        "GladesTown.BelowHoleHutEX",
        "GladesTown.KeyMokiHutEX",
        "GladesTown.AboveTpEX",
        "GladesTown.AboveCaveEX",
        "GladesTown.LupoSwimLeftEX",
        "GladesTown.UpdraftCeilingEX",
        "GladesTown.LeafPileEX",
        "GladesTown.DamageTree",
        "WestGlades.GrappleEX",
        "WestGlades.AbovePlantEX",
        "WestGlades.LowerPoolEX",
        "WestGlades.UpperPoolEX",
        "WestGlades.SwimEC",
        "WestGlades.LeftOre",
        "WestGlades.RightOre",
        "WestGlades.ShrineHC",
        "WestGlades.CombatShrine",
        "OuterWellspring.RightWallOre",
        "OuterWellspring.RightWallEC",
        "OuterWellspring.RightWallEX",
        "OuterWellspring.TrialOre",
        "OuterWellspring.UltraGrappleShard",
        "OuterWellspring.HiddenHC",
        "OuterWellspring.EntranceRoofEX",
        "OuterWellspring.WheelEX",
        "OuterWellspring.BasementEC",
        "OuterWellspring.LifeHarvestShard",
        "OuterWellspring.SwimEX",
        "OuterWellspring.SwimOre",
        "InnerWellspring.ThornShard",
        "InnerWellspring.ThornEX",
        "InnerWellspring.ThreeWheelsEX",
        "InnerWellspring.WaterSwitchEX",
        "InnerWellspring.DrainHC",
        "InnerWellspring.DrainEX",
        "InnerWellspring.LaserOre",
        "InnerWellspring.LeverEC",
        "InnerWellspring.LupoEX",
        "InnerWellspring.LupoMap",
        "InnerWellspring.ShortcutWheelEX",
        "InnerWellspring.GrappleTreeEX",
        "InnerWellspring.GrappleTree",
        "InnerWellspring.AboveSpinArenaEX",
        "InnerWellspring.RotateRoomEX",
        "InnerWellspring.RotateRoomOre",
        "InnerWellspring.LibraryEX",
        "InnerWellspring.AboveTpEX",
        "InnerWellspring.SwimOre",
        "InnerWellspring.EscapeRevisitEX",
        "PoolsApproach.MarshPathCurrentEX",
        "PoolsApproach.AboveWheelEX",
        "PoolsApproach.MillPathHC",
        "PoolsApproach.MillPathEC",
        "PoolsApproach.MillPathEX",
        "EastPools.RightOre",
        "EastPools.TwoCrushersEX",
        "EastPools.BubbleCurrentEX",
        "EastPools.BelowLeverEX",
        "EastPools.AboveDoorOre",
        "EastPools.PurpleWallHC",
        "EastPools.AboveTpEX",
        "EastPools.LupoOre",
        "EastPools.UltraBashShard",
        "EastPools.FightRoomHC",
        "EastPools.EnergyHarvestShard",
        "EastPools.LupoEX",
        "EastPools.LupoMap",
        "EastPools.BehindCrusherEX",
        "UpperPools.LowerKS",
        "UpperPools.UpperLeftKS",
        "UpperPools.UpperMidKS",
        "UpperPools.UpperRightKS",
        "UpperPools.FishPoolEX",
        "UpperPools.FishPoolOre",
        "UpperPools.BubblesEC",
        "UpperPools.RightBubblesEX",
        "UpperPools.LeftBubblesEX",
        "UpperPools.SwimDashTree",
        "UpperPools.SwimDashCurrentEX",
        "UpperPools.RoofEX",
        "UpperPools.WaterfallEC",
        "WestPools.BurrowEX",
        "WestPools.BurrowOre",
        "WestPools.TpEX",
        "WestPools.EscapeRevisitEX",
        "WoodsEntry.MudPitEX",
        "WoodsEntry.LedgeOre",
        "WoodsEntry.LeafPileEX",
        "WoodsEntry.TpEX",
        "WoodsEntry.LowerKS",
        "WoodsEntry.UpperKS",
        "WoodsMain.RightKS",
        "WoodsMain.UpperKS",
        "WoodsMain.LeftKS",
        "WoodsMain.LowerKS",
        "WoodsMain.BehindWallOre",
        "WoodsMain.LowerLeafPileEX",
        "WoodsMain.MiddleLeafPileEX",
        "WoodsMain.UpperLeafPileEX",
        "WoodsMain.YellowWallEX",
        "WoodsMain.HiddenOre",
        "WoodsMain.HiddenEX",
        "WoodsMain.BelowKeystonesEX",
        "WoodsMain.BehindDoorRoofEX",
        "WoodsMain.PetrifiedHowlEX",
        "WoodsMain.OverflowShard",
        "WoodsMain.CombatShrine",
        "WoodsMain.ShrineEX",
        "WoodsMain.FeedingGroundsEX",
        "LowerReach.BelowBaurEX",
        "LowerReach.AboveBaurLowerEX",
        "LowerReach.AboveBaurUpperEX",
        "LowerReach.IcefallOre",
        "LowerReach.IcefallEX",
        "LowerReach.AboveDoorEX",
        "LowerReach.HiddenOre",
        "LowerReach.LupoMap",
        "LowerReach.MeltIceEX",
        "LowerReach.BurrowEX",
        "LowerReach.TPLeftEX",
        "LowerReach.BelowLupoEX",
        "LowerReach.BreakWallEX",
        "LowerReach.WindBottomEX",
        "LowerReach.WindHiddenEX",
        "LowerReach.SnowballHC",
        "LowerReach.RoofLeftEX",
        "LowerReach.RoofRightEX",
        "LowerReach.FractureShard",
        "LowerReach.EscapeRevisitEX",
        "LowerReach.RightKS",
        "LowerReach.UpperLeftKS",
        "LowerReach.MiddleLeftKS",
        "LowerReach.BottomLeftKS",
        "LowerReach.TrialEX",
        "LowerReach.CatalystShard",
        "UpperReach.LifeForceShard",
        "UpperReach.LifeForceEX",
        "UpperReach.LowerKS",
        "UpperReach.UpperKS",
        "UpperReach.MiddleLeftKS",
        "UpperReach.MiddleRightKS",
        "UpperReach.SoupOre",
        "UpperReach.SwingPoleEX",
        "UpperReach.SwimEX",
        "UpperReach.LightBurstTree",
        "UpperReach.TreeOre",
        "UpperReach.WellEX",
        "UpperReach.HiddenEX",
        "UpperDepths.EntrySpikesEX",
        "UpperDepths.EntryRoofEX",
        "UpperDepths.EntryOre",
        "UpperDepths.RightEntryKS",
        "UpperDepths.LeftEntryKS",
        "UpperDepths.SwimEC",
        "UpperDepths.TeleporterEX",
        "UpperDepths.LeftHealthKS",
        "UpperDepths.RightHealthKS",
        "UpperDepths.BossPathEX",
        "UpperDepths.KeystoneHC",
        "UpperDepths.HiveEX",
        "LowerDepths.RaceStartHC",
        "LowerDepths.BelowDoorOre",
        "LowerDepths.SpiritSurgeShard",
        "LowerDepths.CombatShrine",
        "LowerDepths.SwimEC",
        "LowerDepths.LupoMap",
        "LowerDepths.LeftEX",
        "LowerDepths.RightEX",
        "LowerDepths.FlashTree",
        "LowerWastes.WestTPOre",
        "LowerWastes.PurpleWallEX",
        "LowerWastes.SunsetViewEX",
        "LowerWastes.SandBridgeOre",
        "LowerWastes.MuncherTunnelEC",
        "LowerWastes.SandPotHC",
        "LowerWastes.SandPotEX",
        "LowerWastes.MuncherPitEX",
        "LowerWastes.BottomRightEX",
        "LowerWastes.BottomRightHC",
        "LowerWastes.LastStandShard",
        "LowerWastes.LastStandEX",
        "LowerWastes.MuncherClimbEX",
        "LowerWastes.SkeetoHiveEX",
        "LowerWastes.LupoMap",
        "LowerWastes.BurrowTree",
        "LowerWastes.BurrowTreeEX",
        "LowerWastes.UpperPathEC",
        "LowerWastes.UpperPathEX",
        "LowerWastes.UpperPathHiddenEX",
        "LowerWastes.UpperPathHC",
        "LowerWastes.EastTPOre",
        "UpperWastes.LowerKS",
        "UpperWastes.UpperKS",
        "UpperWastes.TurmoilShard",
        "UpperWastes.KSDoorEX",
        "UpperWastes.LedgeEC",
        "UpperWastes.MissileSpawnEX",
        "UpperWastes.PurpleWallEX",
        "UpperWastes.PurpleWallHC",
        "UpperWastes.RoofEX",
        "UpperWastes.SpinLasersRightEX",
        "UpperWastes.SpinLasersMiddleEX",
        "UpperWastes.SpinLasersLowerEX",
        "UpperWastes.WallOre",
        "WindtornRuins.EscapeRevisitEC",
        "WeepingRidge.Ore",
        "WeepingRidge.LaunchTree",
        "WeepingRidge.SpikeClimbEX",
        "WeepingRidge.PortalEX",
        "WillowsEnd.SpikesOre",
        "WillowsEnd.EntryEX",
        "WillowsEnd.PoisonfallHC",
        "WillowsEnd.LupoMap",
        "WillowsEnd.WindSpinOre",
        "WillowsEnd.RedirectEX",
        "WillowsEnd.UpperLeftEX",
        "WillowsEnd.UpperRightEX",
        "TwillenShop.Overcharge",
        "TwillenShop.TripleJump",
        "TwillenShop.Wingclip",
        "TwillenShop.Swap",
        "TwillenShop.LightHarvest",
        "TwillenShop.Vitality",
        "TwillenShop.Energy",
        "TwillenShop.Finesse",
        "OpherShop.WaterBreath",
        "OpherShop.Spike",
        "OpherShop.SpiritSmash",
        "OpherShop.Teleport",
        "OpherShop.SpiritStar",
        "OpherShop.Blaze",
        "OpherShop.Sentry",
        "OpherShop.ExplodingSpike",
        "OpherShop.ShockSmash",
        "OpherShop.StaticStar",
        "OpherShop.ChargeBlaze",
        "OpherShop.RapidSentry",
        "LupoShop.HCMapIcon",
        "LupoShop.ECMapIcon",
        "LupoShop.ShardMapIcon"]
    }
