from fridge import Fridge
from meal import Meal, NutritionalInfo, ServingSize


def test_from_dict(tortilla_nutrition_dict: dict, tortilla_nutrition):
    fridge_dict = {"meals": {"tortilla": tortilla_nutrition_dict}}
    fridge = Fridge({"tortilla": tortilla_nutrition})
    assert fridge == Fridge.from_dict(fridge_dict)


def test_get_meal(fridge: Fridge, tortilla: Meal):
    assert fridge.get_meal(tortilla.name) == tortilla


def test_get_random_meal(fridge: Fridge):
    """Test the random meal exists in Fridge and it is unchanged."""
    random_meal = fridge.get_random_meal()
    assert fridge.get_meal(random_meal.name) == random_meal


def test_add_meal(fridge: Fridge):
    serving = ServingSize("grams", 50)
    nutrition = NutritionalInfo(serving, fats=5, carbs=0, proteins=6)
    eggs = Meal("eggs", nutrition)

    fridge.add_meal(eggs)
    assert fridge.get_meal(eggs.name) == eggs


def test_pop_meal(fridge: Fridge, tortilla: Meal):
    assert tortilla == fridge.pop_meal(tortilla.name)
