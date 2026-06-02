import pytest

from food import Food, NutritionalInfo, ServingSize
from pantry import Pantry


@pytest.fixture
def pantry_dict(tortilla_nutrition_dict: dict) -> dict:
    return {
        "foods": {
            "tortilla": tortilla_nutrition_dict,
        }
    }


@pytest.fixture
def tortilla(tortilla_nutrition: NutritionalInfo) -> Food:
    return Food(name="tortilla", nutrition=tortilla_nutrition)


@pytest.fixture
def pantry(tortilla_nutrition: NutritionalInfo) -> Pantry:
    return Pantry({"tortilla": tortilla_nutrition})


def test_from_dict(pantry: Pantry, pantry_dict: dict):
    assert pantry == Pantry.from_dict(pantry_dict)


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
