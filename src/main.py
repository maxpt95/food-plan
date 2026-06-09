"""Entry point of Meal Prep

Where the user interface lives.
Most I/O operations should be concentrated here.
"""

import json
import time
from copy import deepcopy
from dataclasses import asdict

import config
import prep
from constants import MENU_OPTIONS_NUMBER, SEPARATOR
from meal import Meal, NutritionalInfo, ServingSize
from pantry import Pantry


def ask_nutritional_info() -> NutritionalInfo:
    while True:
        print("\nInsert meal nutritional information.")
        serving_amount = int(input("Serving size amount: "))
        serving_unit = input("Serving size unit: ")
        fats = float(input("Fats (g): "))
        carbs = float(input("Carbs (g): "))
        proteins = float(input("Protein (g): "))

        try:
            serving = ServingSize(serving_amount, serving_unit)
            return NutritionalInfo(serving, fats, carbs, proteins)
        except ValueError as e:
            print(f"\n{e}")


def ask_meal_name() -> str:
    meal_name = input("Enter meal name: ").lower().strip()
    if not meal_name:
        print("\nmeal name is empty")

    return meal_name


def add_meal(pantry: Pantry, meal_name: str):
    """Add meal user interface.

    Adds a new meal to pantry.

    Args:
        pantry: the pantry instance to interact
        with the meal inventory.
        meal_name: name of the meal to add to the pantry.
    """
    nutrition = ask_nutritional_info()
    meal = Meal(meal_name, nutrition)
    pantry.add_meal(meal)
    print(f"\nAdded to pantry:\n{meal}")


def modify_meal(pantry: Pantry, meal: Meal) -> None:
    meal_name = meal.name
    while True:
        print(f"\nModifying {meal.name.title()}.")
        print(SEPARATOR)
        print("1. Name")
        print("2. Serving Size")
        print("3. Protein")
        print("4. Fats")
        print("5. Carbs")
        print("6. All nutritional info")
        print("7. EXIT")

        choice = int(input("\n Choose: "))

        match choice:
            case 1:
                new_name = ask_meal_name()
                if not new_name:
                    continue
                meal.name = new_name
            case 2:
                serving_size = meal.nutrition.serving_size
                print(f"\n{meal.name} {serving_size}")
                try:
                    serving_size.amount = float(
                        input("Enter new serving size amount: ")
                    )
                except ValueError as e:
                    print(f"\n{e}")
                    continue
                serving_size.unit = input("Enter new serving size unit: ")
            case 3:
                print(f"\n{meal.name} current proteins(g): {meal.nutrition.proteins}")
                try:
                    meal.nutrition.proteins = float(
                        input("Enter new protein(g) amount: ")
                    )
                except ValueError as e:
                    print(f"\n{e}")
            case 4:
                print(f"\n{meal.name} current carbs(g): {meal.nutrition.fats}")
                try:
                    meal.nutrition.fats = float(input("Enter new fats(g) amount: "))
                except ValueError as e:
                    print(f"\n{e}")
            case 5:
                print(f"\n{meal.name} current carbs(g): {meal.nutrition.carbs}")
                try:
                    meal.nutrition.carbs = float(input("Enter new carbs(g) amount: "))
                except ValueError as e:
                    print(f"\n{e}")
            case 6:
                meal.nutrition = ask_nutritional_info()
            case 7:
                pantry.pop_meal(meal_name)
                pantry.add_meal(meal)
                return
            case _:
                print(f"Invalid option: {choice}")


def list_meals(pantry: Pantry) -> None:
    if not pantry.meals:
        print("\nYour pantry is empty. Try adding some meals!")
        return

    print("\nThis is your pantry:\n")
    print(pantry)


def remove_meal(pantry: Pantry) -> None:
    meal_name = input("Enter meal name to be removed: ")
    meal = pantry.pop_meal(meal_name)

    if not meal:
        print(f"\n{meal_name} wasn't found in pantry.")

    print(f"\nRemoved {meal_name} from pantry.")


def prepare_meal(pantry: Pantry) -> None:
    if not pantry.meals:
        print("\nYour pantry is empty. Try adding some meals!")
        return

    pantry_cp = deepcopy(pantry)
    calory_budget = float(input("\nEnter your calory budget: "))

    while True:
        print("\nPreparing meal...")
        meal = prep.prepare_meal(pantry_cp, calory_budget)

        print(f"\nHere is a meal that fits your calory budget of {calory_budget}kcal")
        print(f"\n{meal}")
        print("\nWould you like a different meal?")
        repeat = input("Yes/No: ").lower()

        if repeat == "no":
            return
        # pop the recommendation to not repeat again
        pantry_cp.pop_meal(meal.name)


def route_request(request: int, pantry: Pantry) -> None:
    match request:
        case 1:
            list_meals(pantry)
        case 2:
            meal_name = ask_meal_name()
            meal = pantry.get_meal(meal_name)
            if not meal:
                add_meal(pantry, meal_name)
                return
            modify_meal(pantry, meal)
        case 3:
            remove_meal(pantry)
        case 4:
            prepare_meal(pantry)
        case _:
            raise ValueError(f"invalid request: {request}")


def menu() -> None:
    print("\nMeal Prep")
    print(SEPARATOR)
    print("1. Show meal list.")
    print("2. Add or modify meal.")
    print("3. Remove meal.")
    print("4. Prepare a meal!")
    print("5. EXIT.")


def main():
    print("Welcome to Meal Prep!")
    print("Loading pantry...")

    if not config.PANTRY_PATH.exists():
        config.PANTRY_PATH.write_text("{}", encoding="utf-8")

    pantry = Pantry.from_dict(json.load(config.PANTRY_PATH.open()))
    while True:
        time.sleep(1)
        menu()
        try:
            request = int(input("\nChoose an option number: "))
        except ValueError:
            print("\nPlease choose one of the listed option numbers.")
            continue

        # chose to exit.
        if request == MENU_OPTIONS_NUMBER:
            with open(config.PANTRY_PATH, "w") as f:
                json.dump(asdict(pantry), f)

            return

        try:
            route_request(request, pantry)
        except ValueError:
            print("\nPlease choose one of the listed options")


if __name__ == "__main__":
    main()
