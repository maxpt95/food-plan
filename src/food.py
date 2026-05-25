from dataclasses import dataclass


@dataclass
class ServingSize:
    amount: float
    unit: str


@dataclass
class NutritionalInfo:
    serving_size: ServingSize
    fats: float
    carbs: float
    proteins: float

    def __str__(self):
        return f"""
Fats: {self.fats}g
Carbohidrates: {self.carbs}g
Proteins: {self.proteins}g
"""


@dataclass
class Food:
    name: str
    nutrition: NutritionalInfo | None = None

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Food name can't be empty.")
