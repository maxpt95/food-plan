from food import Food, NutritionalInfo, ServingSize
from pantry import Pantry


def test_from_dict(tortilla_nutrition_dict: dict, tortilla_nutrition):
    pantry_dict = {"foods": {"tortilla": tortilla_nutrition_dict}}
    pantry = Pantry({"tortilla": tortilla_nutrition})
    assert pantry == Pantry.from_dict(pantry_dict)


def test_get_food(pantry: Pantry, tortilla: Food):
    assert pantry.get_food(tortilla.name) == tortilla


def test_get_random_food(pantry: Pantry):
    """Test the random food exists in Pantry and it is unchanged."""
    random_food = pantry.get_random_food()
    assert pantry.get_food(random_food.name) == random_food


def test_add_food(pantry: Pantry):
    serving = ServingSize(50, "grams")
    nutrition = NutritionalInfo(serving, fats=5, carbs=0, proteins=6)
    eggs = Food("eggs", nutrition)

    pantry.add_food(eggs)
    assert pantry.get_food(eggs.name) == eggs


def test_pop_food(pantry: Pantry, tortilla: Food):
    assert tortilla == pantry.pop_food(tortilla.name)
