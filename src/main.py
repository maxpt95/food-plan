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
from constants import MAIN_MENU_OPTIONS_NUMBER, SEPARATOR
from fridge import Fridge
from meal import Meal, NutritionalInfo, ServingSize


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


def ask_choice(max_options: int) -> int:
    """Request an option choice for all menus.

    Args:
        max_choice: maximum number of options available to
            choose from.
    Returns:
        A valid user choice or -1 if the choice is invalid.
    """
    CHOOSE_AGAIN_MSG = "\nPlease choose one of the listed option numbers."
    try:
        choice = int(input("\nChoose an option number: "))
    except ValueError:
        print(CHOOSE_AGAIN_MSG)
        return -1

    if 0 < choice <= max_options:
        print(CHOOSE_AGAIN_MSG)
        return choice

    return -1


def add_meal(fridge: Fridge, meal_name: str):
    """Add meal user interface.

    Adds a new meal to fridge.

    Args:
        fridge: the fridge instance to interact
        with the meal inventory.
        meal_name: name of the meal to add to the fridge.
    """
    nutrition = ask_nutritional_info()
    meal = Meal(meal_name, nutrition)
    fridge.add_meal(meal)
    print(f"\nAdded to fridge:\n{meal}")


def modify_meal(fridge: Fridge, meal: Meal) -> None:
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

        choice = ask_choice(max_options=7)

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
                fridge.pop_meal(meal_name)
                fridge.add_meal(meal)
                return
            case _:
                print(f"Invalid option: {choice}")


def list_meals(fridge: Fridge) -> None:
    if not fridge.meals:
        print("\nYour fridge is empty. Try adding some meals!")
        return

    print("\nThis is your fridge:\n")
    print(fridge)


def remove_meal(fridge: Fridge) -> None:
    meal_name = input("Enter meal name to be removed: ")
    meal = fridge.pop_meal(meal_name)

    if not meal:
        print(f"\n{meal_name} wasn't found in fridge.")

    print(f"\nRemoved {meal_name} from fridge.")


def prepare_meal(fridge: Fridge) -> None:
    if not fridge.meals:
        print("\nYour fridge is empty. Try adding some meals!")
        return

    fridge_cp = deepcopy(fridge)
    calory_budget = float(input("\nEnter your calory budget: "))

    while True:
        print("\nPreparing meal...")
        meal = prep.prepare_meal(fridge_cp, calory_budget)

        print(f"\nHere is a meal that fits your calory budget of {calory_budget}kcal")
        print(f"\n{meal}")
        print("\nWould you like a different meal?")
        repeat = input("Yes/No: ").lower()

        if repeat == "no":
            return
        # pop the recommendation to not repeat again
        fridge_cp.pop_meal(meal.name)


def route_choice(request: int, fridge: Fridge) -> None:
    match request:
        case 1:
            list_meals(fridge)
        case 2:
            meal_name = ask_meal_name()
            meal = fridge.get_meal(meal_name)
            if not meal:
                add_meal(fridge, meal_name)
                return
            modify_meal(fridge, meal)
        case 3:
            remove_meal(fridge)
        case 4:
            # prepare_meal_menu(fridge)
            pass
        case _:
            raise ValueError(f"invalid request: {request}")


def main_menu() -> int:
    while True:
        time.sleep(config.BASE_WAIT_TIME_SEC)

        print("\nMeal Prep")
        print(SEPARATOR)
        print("1. Show meal list.")
        print("2. Add or modify meal.")
        print("3. Remove meal.")
        print("4. Prep a random meal.")
        print("5. Prep a meal of my choice.")
        print("6. EXIT.")

        if (choice := ask_choice(max_options=MAIN_MENU_OPTIONS_NUMBER)) != -1:
            return choice


def main():
    print("Welcome to Meal Prep!")
    print("Loading fridge...")

    if not config.PANTRY_PATH.exists():
        config.PANTRY_PATH.write_text("{}", encoding="utf-8")

    fridge = Fridge.from_dict(json.load(config.PANTRY_PATH.open()))
    while True:
        choice = main_menu()

        # chose to exit.
        if choice == MAIN_MENU_OPTIONS_NUMBER:
            with open(config.PANTRY_PATH, "w") as f:
                json.dump(asdict(fridge), f, indent=4)
            return

        route_choice(choice, fridge)


if __name__ == "__main__":
    main()
