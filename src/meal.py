from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass


@dataclass
class ServingSize:
    unit: str
    amount: float

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount can't be negative")

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float):
        """Sets only positive amounts."""
        if value < 0:
            raise ValueError("Amount can't be negative")
        self._amount = value

    def __str__(self):
        return f"Serving Size: {self.amount:.2f}{self.unit}"


@dataclass
class NutritionalInfo:
    serving_size: ServingSize
    fats: float
    carbs: float
    proteins: float

    def __post_init__(self):
        """Validate macronutrients are positive."""
        if self.fats < 0 or self.carbs < 0 or self.proteins < 0:
            raise ValueError("Fats, carbs and proteins can't be negative")

    @classmethod
    def from_dict(cls, nutritional_info: dict):
        nutritional_info_cp = deepcopy(nutritional_info)
        serving_size = ServingSize(**nutritional_info_cp.pop("serving_size"))
        return cls(serving_size, **nutritional_info_cp)

    @property
    def fats(self) -> float:
        return self._fats

    @fats.setter
    def fats(self, value: float) -> None:
        if value < 0:
            raise ValueError("fats can't be negative")
        self._fats = value

    @property
    def carbs(self) -> float:
        return self._carbs

    @carbs.setter
    def carbs(self, value: float) -> None:
        if value < 0:
            raise ValueError("carbs can't be negative")
        self._carbs = value

    @property
    def proteins(self) -> float:
        return self._proteins

    @proteins.setter
    def proteins(self, value: float) -> None:
        if value < 0:
            raise ValueError("proteins can't be negative")
        self._proteins = value

    def __str__(self):
        return f"""Nutritional Info
------------------
{self.serving_size}
------------------
Fats: {self.fats:.2f}g
Carbohydrates: {self.carbs:.2f}g
Proteins: {self.proteins:.2f}g
"""


@dataclass
class Meal:
    name: str
    nutrition: NutritionalInfo

    def __str__(self):
        return f"{self.name.title()}\n------------------\n{self.nutrition}"
