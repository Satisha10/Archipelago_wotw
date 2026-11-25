from rule_builder.rules import Rule, Has, True_, Atleast

def has_any_elements(count) -> Rule:
    return AtLeast(count, Has("Physis"), Has("Aether"), Has("Cryo"))  # Has("Ignis")

def has_area_unlock(name: str) -> Rule:
    if name == "valley":
        return True_()
    if name == "aether":
        return Has("Area unlock", count=1) | Has("Dungeon unlock", count=1) | Has("Trial of Aether unlock")
    if name == "plains":
        return Has("Area unlock", count=2) | Has("Overworld Area unlock", count=1) | Has("Aurum Plains unlock")
    if name == "swamp":
        return Has("Area unlock", count=3) | Has("Overworld Area unlock", count=2) | Has("Scala Moor unlock")
    if name == "cryo":
        return Has("Area unlock", count=4) | Has("Dungeon unlock", count=2) | Has("Trial of Cryo unlock")
    raise ValueError(f"{name=} is not a valid area name.")
