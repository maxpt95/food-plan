import pytest

from meal import Meal, NutritionalInfo, ServingSize
from pantry import Pantry


@pytest.fixture
def tortilla_nutrition_dict() -> dict:
    return {
        "serving_size": {"unit": "grams", "amount": 60},
        "fats": 4,
        "carbs": 27,
        "proteins": 6,
    }


@pytest.fixture
def tortilla_serving(tortilla_nutrition_dict: dict) -> ServingSize:
    return ServingSize(**tortilla_nutrition_dict["serving_size"])


@pytest.fixture
def tortilla_nutrition(tortilla_nutrition_dict: dict) -> NutritionalInfo:
    return NutritionalInfo.from_dict(tortilla_nutrition_dict)


@pytest.fixture
def tortilla(tortilla_nutrition: NutritionalInfo) -> Meal:
    return Meal(name="tortilla", nutrition=tortilla_nutrition)


@pytest.fixture
def pantry_dict(tortilla_nutrition_dict: dict) -> dict:
    return {
        "meals": {
            "tortilla": tortilla_nutrition_dict,
            "spaghetti": {
                "serving_size": {"unit": "g", "amount": 100},
                "fats": 1.5,
                "carbs": 75,
                "proteins": 13,
            },
            "rice": {
                "serving_size": {"unit": "g", "amount": 100},
                "fats": 0.7,
                "carbs": 80,
                "proteins": 7.1,
            },
        }
    }


@pytest.fixture
def pantry(tortilla_nutrition: NutritionalInfo, pantry_dict: dict) -> Pantry:
    return Pantry.from_dict(pantry_dict)
