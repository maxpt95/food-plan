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
def tortilla(tortilla_nutrition: NutritionalInfo) -> Food:
    return Food(name="tortilla", nutrition=tortilla_nutrition)


@pytest.fixture
def pantry() -> Pantry:
    return Pantry.from_dict(PANTRY_DICT)


def test_from_dict(pantry: Pantry):
    assert pantry == Pantry.from_dict(PANTRY_DICT)


def test_get_food(pantry: Pantry, tortilla: Food):
    assert pantry.get_food(tortilla.name) == tortilla


def test_add_food(pantry: Pantry):
    serving = ServingSize(50, "grams")
    nutrition = NutritionalInfo(serving, fats=5, carbs=0, proteins=6)
    eggs = Food("eggs", nutrition)

    pantry.add_food(eggs)
    assert pantry.get_food(eggs.name) == eggs


def test_pop_food(pantry: Pantry, tortilla: Food):
    assert tortilla == pantry.pop_food(tortilla.name)
