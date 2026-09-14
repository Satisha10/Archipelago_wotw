from rule_builder.rules import Rule, HasAll#, Has, Atleast

def has_any_elements(count) -> Rule:
    return HasAll("Physis", "Aether")

    # TODO Use AtLeast once AP is at 0.6.8
    # return AtLeast(count, Has("Physis"), Has("Aether"))  # Has("Cryo"), Has("Ignis")
