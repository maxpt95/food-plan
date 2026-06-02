import pytest

from food import NutritionalInfo, ServingSize


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
