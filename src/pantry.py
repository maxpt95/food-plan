from __future__ import annotations
from dataclasses import dataclass

from food import Food, NutritionalInfo

FoodName = str


@dataclass
class Pantry:
    foods: dict[FoodName, NutritionalInfo]

    @classmethod
    def from_json(cls, foods_json: dict) -> Pantry:
        """Instantiates Pantry from a json dict"""
        return cls(
            foods={
                food_name: NutritionalInfo(**nutrition)
                for food_name, nutrition in foods_json["foods"].items()
            }
        )

    def add_food(self, food: Food) -> None:
        self.foods[food.name] = food.nutrition

    def get_food(self, food: Food) -> Food | None:
        nutrition = self.foods.get(food.name)
        return Food(food.name, nutrition) if nutrition is not None else None

    def pop_food(self, food_name: str) -> Food | None:
        """Remove food from pantry

        Returns:
            The food item removed or None if it doesn't exist.
        """
        try:
            return self.foods.popitem(food_name)
        except KeyError:
            return None

    def __str__(self):
        return "\n\n".join(
            f"{food_name}\np: {nutrition.proteins}|f: {nutrition.fats}|c: {nutrition.carbs}"
            for food_name, nutrition in self.foods.items()
        )
