from dataclasses import dataclass

from food import Food, NutritionalInfo

FoodName = str


@dataclass
class Pantry:
    foods: dict[FoodName, NutritionalInfo]

    def add_food(self, food: Food):
        self.foods[food.name] = food.nutrition

    def get_food(self, food: Food) -> Food | None:
        nutrition = self.foods.get(food.name)
        return Food(food.name, nutrition) if nutrition is not None else None

    def __str__(self):
        return "\n".join(
            f"{food_name}:\n{nutrition}" for food_name, nutrition in self.foods.items()
        )
