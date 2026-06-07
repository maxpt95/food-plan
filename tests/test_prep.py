from unittest.mock import create_autospec

import prep
from food import Food, NutritionalInfo
from pantry import Pantry


def test_calculate_calories(tortilla_nutrition: NutritionalInfo):

    tortilla_calories = prep.calculate_calories(tortilla_nutrition)

    assert tortilla_calories == 168


def test_resize_meal(tortilla: Food):
    resized = prep.resize_meal(tortilla, 0.25)

    assert resized.name == "tortilla"
    assert resized.nutrition.carbs == tortilla.nutrition.carbs * 0.25
    assert resized.nutrition.proteins == tortilla.nutrition.proteins * 0.25
    assert resized.nutrition.fats == tortilla.nutrition.fats * 0.25


def test_prepare_meal(tortilla: Food):
    pantry = create_autospec(
        Pantry
    )  # mock Pantry because we need to make get_random_food deterministic
    pantry.get_random_food.return_value = tortilla

    meal = prep.prepare_meal(pantry, calory_budget=1680)

    assert meal.name == tortilla.name
    assert meal.nutrition.carbs == tortilla.nutrition.carbs * 10
    assert meal.nutrition.proteins == tortilla.nutrition.proteins * 10
    assert meal.nutrition.fats == tortilla.nutrition.fats * 10
