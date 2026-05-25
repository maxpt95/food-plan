from dataclasses import dataclass


@dataclass
class NutritionalInfo:
    fats: float
    carbs: float
    proteins: float


@dataclass
class Food:
    name: str
    nutrition: NutritionalInfo | None = None

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Food name can't be empty.")
