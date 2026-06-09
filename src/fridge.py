from __future__ import annotations

import random
from dataclasses import dataclass

from meal import Meal, NutritionalInfo

MealName = str


@dataclass
class Fridge:
    meals: dict[MealName, NutritionalInfo]

    @classmethod
    def from_dict(cls, fridge_dict: dict) -> Fridge:
        """Instantiates Fridge from a json dict"""
        return cls(
            meals={
                meal_name: NutritionalInfo.from_dict(nutrition)
                for meal_name, nutrition in fridge_dict["meals"].items()
            }
        )

    def add_meal(self, meal: Meal) -> None:
        self.meals[meal.name] = meal.nutrition

    def get_meal(self, meal_name: str) -> Meal | None:
        nutrition = self.meals.get(meal_name.lower())
        return Meal(meal_name, nutrition) if nutrition is not None else None

    def get_random_meal(self) -> Meal | None:
        if not self.meals:
            return None

        random_meal = random.choice(tuple(self.meals.items()))

        return Meal(name=random_meal[0], nutrition=random_meal[1])

    def pop_meal(self, meal_name: str) -> Meal | None:
        """Remove meal from fridge

        Returns:
            The meal item removed or None if it doesn't exist.
        """
        try:
            nutrition = self.meals.pop(meal_name.lower())
        except KeyError:
            return None

        return Meal(meal_name, nutrition)

    def __str__(self):
        return "\n\n".join(
            f"{meal_name.capitalize()}\np: {nutrition.proteins}|f: {nutrition.fats}|c: {nutrition.carbs}"
            for meal_name, nutrition in self.meals.items()
        )
