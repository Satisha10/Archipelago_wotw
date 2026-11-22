from rule_builder.rules import Rule, HasAll, Has, True_#, Atleast

def has_any_elements(count) -> Rule:
    return HasAll("Physis", "Aether") | HasAll("Physis", "Cryo") | HasAll("Aether", "Cryo")

    # TODO Use AtLeast once AP is at 0.6.8
    # return AtLeast(count, Has("Physis"), Has("Aether"))  # Has("Cryo"), Has("Ignis")

def has_area_unlock(name: str) -> Rule:
    if name == "valley":
        return True_()
    if name == "aether":
        return Has("Area unlock", count=1) | Has("Dungeon unlock", count=1)
    if name == "plains":
        return Has("Area unlock", count=2) | Has("Overworld Area unlock", count=1)
    if name == "swamp":
        return Has("Area unlock", count=3) | Has("Overworld Area unlock", count=2)
    if name == "cryo":
        return Has("Area unlock", count=4) | Has("Dungeon unlock", count=2)
    raise ValueError(f"{name=} is not a valid area name.")
