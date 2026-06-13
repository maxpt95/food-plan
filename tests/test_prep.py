from unittest.mock import create_autospec

import prep
from fridge import Fridge
from meal import Meal, NutritionalInfo


def test_calculate_calories(tortilla_nutrition: NutritionalInfo):

    tortilla_calories = prep.calculate_calories(tortilla_nutrition)

    assert tortilla_calories == 168


def test_resize_meal(tortilla: Meal):
    resized = prep.resize_meal(tortilla, 0.25)

    assert resized.name == "tortilla"
    assert resized.nutrition.carbs == tortilla.nutrition.carbs * 0.25
    assert resized.nutrition.proteins == tortilla.nutrition.proteins * 0.25
    assert resized.nutrition.fats == tortilla.nutrition.fats * 0.25


def test_prepare_meal(tortilla: Meal):
    fridge = create_autospec(
        Fridge
    )  # mock Fridge because we need to make get_random_meal deterministic
    fridge.get_random_meal.return_value = tortilla

    meal = prep.prepare_meal(fridge, calorie_budget=1680)

    assert meal.name == tortilla.name
    assert meal.nutrition.carbs == tortilla.nutrition.carbs * 10
    assert meal.nutrition.proteins == tortilla.nutrition.proteins * 10
    assert meal.nutrition.fats == tortilla.nutrition.fats * 10
