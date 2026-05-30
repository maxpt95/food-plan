from dataclasses import dataclass
from copy import deepcopy


# TODO: validate amount is positive
@dataclass
class ServingSize:
    amount: float
    unit: str

    def __str__(self):
        return f"Serving Size: {self.amount}{self.unit}"


# TODO: validate macronutrients are positive
@dataclass
class NutritionalInfo:
    serving_size: ServingSize
    fats: float
    carbs: float
    proteins: float

    @classmethod
    def from_dict(cls, nutritional_info: dict):
        nutritional_info_cp = deepcopy(nutritional_info)
        serving_size = ServingSize(**nutritional_info_cp.pop("serving_size"))
        return cls(serving_size, **nutritional_info_cp)

    def __str__(self):
        return f"""Nutritional Info
------------------
{self.serving_size}
------------------
Fats: {self.fats}g
Carbohydrates: {self.carbs}g
Proteins: {self.proteins}g
"""


@dataclass
class Food:
    name: str
    nutrition: NutritionalInfo

    def __str__(self):
        return f"{self.name.capitalize()}\n------------------\n{self.nutrition}"
