from fridge import Fridge
from meal import Meal, NutritionalInfo, ServingSize


def calculate_calories(nutrition: NutritionalInfo):
    return nutrition.fats * 9 + nutrition.carbs * 4 + nutrition.proteins * 4


def resize_meal(meal: Meal, ratio: float) -> Meal:
    resized_serving_amount = meal.nutrition.serving_size.amount * ratio
    resized_serving = ServingSize(
        meal.nutrition.serving_size.unit,
        resized_serving_amount,
    )
    resized_nutrition = NutritionalInfo(
        resized_serving,
        meal.nutrition.fats * ratio,
        meal.nutrition.carbs * ratio,
        meal.nutrition.proteins * ratio,
    )
    return Meal(meal.name, resized_nutrition)


def prepare_meal(fridge: Fridge, calorie_budget: float, meal_name: str = "") -> Meal:
    meal = fridge.get_random_meal() if not meal_name else fridge.get_meal(meal_name)

    meal_calories = calculate_calories(meal.nutrition)

    meal_to_budget_ratio = calorie_budget / meal_calories

    return resize_meal(meal, meal_to_budget_ratio)
