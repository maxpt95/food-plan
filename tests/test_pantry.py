import pytest

from food import Food, NutritionalInfo, ServingSize
from pantry import Pantry

TORTILLA_NUTRITION = {
    "serving_size": {"unit": "grams", "amount": 60},
    "fats": 4,
    "carbs": 27,
    "proteins": 6,
}
PANTRY_DICT = {
    "foods": {
        "tortilla": TORTILLA_NUTRITION,
    }
}


@pytest.fixture
def tortilla() -> Food:
    nutrition = NutritionalInfo(**TORTILLA_NUTRITION)
    return Food(name="tortilla", nutrition=nutrition)


@pytest.fixture
def pantry(tortilla: Food) -> Pantry:
    return Pantry(foods={tortilla.name: tortilla.nutrition})


def test_from_dict(pantry: Pantry):
    assert pantry == Pantry.from_dict(PANTRY_DICT)


def test_get_food(pantry: Pantry, tortilla: Food):
    food = pantry.get_food(tortilla)
    assert food.name == food.name


def test_add_food(pantry: Pantry):
    serving = ServingSize(50, "grams")
    nutrition = NutritionalInfo(serving, fats=5, carbs=0, proteins=6)
    food = Food("eggs", nutrition)

    pantry.add_food(food)
    assert pantry.get_food(food).name == "eggs"


def test_pop_food(pantry: Pantry, tortilla: Food):
    assert tortilla == pantry.pop_food(tortilla.name)
