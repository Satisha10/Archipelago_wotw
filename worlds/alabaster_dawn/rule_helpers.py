from rule_builder.rules import AtLeast, Rule, Has

def has_any_elements(count) -> Rule:
    return AtLeast(count, Has("Physis"), Has("Aether"))  # Has("Cryo"), Has("Ignis")
