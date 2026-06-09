from meal import Meal, NutritionalInfo, ServingSize
from pantry import Pantry


def test_from_dict(tortilla_nutrition_dict: dict, tortilla_nutrition):
    pantry_dict = {"meals": {"tortilla": tortilla_nutrition_dict}}
    pantry = Pantry({"tortilla": tortilla_nutrition})
    assert pantry == Pantry.from_dict(pantry_dict)


def test_get_meal(pantry: Pantry, tortilla: Meal):
    assert pantry.get_meal(tortilla.name) == tortilla


def test_get_random_meal(pantry: Pantry):
    """Test the random meal exists in Pantry and it is unchanged."""
    random_meal = pantry.get_random_meal()
    assert pantry.get_meal(random_meal.name) == random_meal


def test_add_meal(pantry: Pantry):
    serving = ServingSize(50, "grams")
    nutrition = NutritionalInfo(serving, fats=5, carbs=0, proteins=6)
    eggs = Meal("eggs", nutrition)

    pantry.add_meal(eggs)
    assert pantry.get_meal(eggs.name) == eggs


def test_pop_meal(pantry: Pantry, tortilla: Meal):
    assert tortilla == pantry.pop_meal(tortilla.name)
