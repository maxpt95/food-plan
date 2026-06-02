from __future__ import annotations

import random
from dataclasses import dataclass

from food import Food, NutritionalInfo

FoodName = str


@dataclass
class Pantry:
    foods: dict[FoodName, NutritionalInfo]

    @classmethod
    def from_dict(cls, pantry_dict: dict) -> Pantry:
        """Instantiates Pantry from a json dict"""
        return cls(
            foods={
                food_name: NutritionalInfo.from_dict(nutrition)
                for food_name, nutrition in pantry_dict["foods"].items()
            }
        )

    def add_food(self, food: Food) -> None:
        self.foods[food.name] = food.nutrition

    def get_food(self, food_name: str) -> Food | None:
        nutrition = self.foods.get(food_name.lower())
        return Food(food_name, nutrition) if nutrition is not None else None

    def get_random_food(self) -> Food | None:
        if not self.foods:
            return None

        random_food = random.choice(tuple(self.foods.items()))

        return Food(name=random_food[0], nutrition=random_food[1])

    def pop_food(self, food_name: str) -> Food | None:
        """Remove food from pantry

        Returns:
            The food item removed or None if it doesn't exist.
        """
        try:
            nutrition = self.foods.pop(food_name.lower())
        except KeyError:
            return None

        return Food(food_name, nutrition)

    def __str__(self):
        return "\n\n".join(
            f"{food_name.capitalize()}\np: {nutrition.proteins}|f: {nutrition.fats}|c: {nutrition.carbs}"
            for food_name, nutrition in self.foods.items()
        )
