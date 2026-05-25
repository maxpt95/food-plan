import pytest

from food import Food, NutritionalInfo, ServingSize
from pantry import Pantry

TORTILLA_NUTRITION = {
    "serving_size": {"unit": "grams", "amount": 60},
    "fats": 4,
    "carbs": 27,
    "proteins": 6,
}


@pytest.fixture
def pantry() -> Pantry:
    pantry_dict = {
        "tortilla": {
            "nutrition": TORTILLA_NUTRITION,
        }
    }
    return Pantry(pantry_dict)


@pytest.fixture
def tortilla() -> Food:
    nutrition = NutritionalInfo(**TORTILLA_NUTRITION)
    return Food(name="tortilla", nutrition=nutrition)


def test_get_food(pantry: Pantry, tortilla: Food):
    food = pantry.get_food(tortilla)
    assert food.name == food.name


def test_add_food(pantry: Pantry):
    serving = ServingSize(50, "grams")
    nutrition = NutritionalInfo(serving, fats=5, carbs=0, proteins=6)
    food = Food("eggs", nutrition)

    pantry.add_food(food)
    assert pantry.get_food(food).name == "eggs"
