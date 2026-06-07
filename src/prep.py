from food import Food, NutritionalInfo, ServingSize
from pantry import Pantry


def calculate_calories(nutrition: NutritionalInfo):
    return nutrition.fats * 9 + nutrition.carbs * 4 + nutrition.proteins * 4


def resize_meal(meal: Food, ratio: float) -> Food:
    resized_serving_amount = meal.nutrition.serving_size.amount * ratio
    resized_serving = ServingSize(
        resized_serving_amount,
        meal.nutrition.serving_size.unit,
    )
    resized_nutrition = NutritionalInfo(
        resized_serving,
        meal.nutrition.fats * ratio,
        meal.nutrition.carbs * ratio,
        meal.nutrition.proteins * ratio,
    )
    return Food(meal.name, resized_nutrition)


def prepare_meal(pantry: Pantry, calory_budget: float) -> Food:
    meal = pantry.get_random_food()

    meal_calories = calculate_calories(meal.nutrition)

    meal_to_budget_ratio = calory_budget / meal_calories

    return resize_meal(meal, meal_to_budget_ratio)
