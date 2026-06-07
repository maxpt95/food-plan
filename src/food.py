from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass


class ServingSize:
    def __init__(self, amount: float, unit: str):
        if amount < 0:
            raise ValueError("Amount can't be negative")
        self._amount = amount
        self.unit = unit

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float):
        """Sets only positive amounts."""
        if value < 0:
            raise ValueError("Amount can't be negative")
        self._amount = value

    def __eq__(self, other: ServingSize) -> bool:
        if not isinstance(other, ServingSize):
            return False

        return other._amount == self._amount and other.unit == self.unit

    def __str__(self):
        return f"Serving Size: {self.amount}{self.unit}"


class NutritionalInfo:
    def __init__(
        self, serving_size: ServingSize, fats: float, carbs: float, proteins: float
    ):
        """Validate macronutrients are positive."""
        if fats < 0 or carbs < 0 or proteins < 0:
            raise ValueError("Fats, carbs and proteins can't be negative")

        self.serving_size = serving_size
        self._fats = fats
        self._carbs = carbs
        self._proteins = proteins

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
        self._fats = self.fats

    @property
    def carbs(self) -> float:
        return self._carbs

    @carbs.setter
    def carbs(self, value: float) -> None:
        if value < 0:
            raise ValueError("carbs can't be negative")
        self._carbs = self.carbs

    @property
    def proteins(self) -> float:
        return self._proteins

    @proteins.setter
    def proteins(self, value: float) -> None:
        if value < 0:
            raise ValueError("proteins can't be negative")
        self._proteins = self.proteins

    def __eq__(self, other: NutritionalInfo) -> bool:
        if not isinstance(other, NutritionalInfo):
            return False

        return (
            other.serving_size == self.serving_size
            and other._fats == self._fats
            and other._carbs == self._carbs
            and other._proteins == self._proteins
        )

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
