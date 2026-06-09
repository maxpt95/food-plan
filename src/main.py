"""Entry point of Food Plan

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
from food import Food, NutritionalInfo, ServingSize
from pantry import Pantry


def ask_nutritional_info() -> NutritionalInfo:
    while True:
        print("\nInsert food nutritional information.")
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


def ask_food_name() -> str:
    food_name = input("Enter food name: ").lower().strip()
    if not food_name:
        print("\nFood name is empty")

    return food_name


def add_food(pantry: Pantry, food_name: str):
    """Add food user interface.

    Adds a new food to pantry.

    Args:
        pantry: the pantry instance to interact
        with the food inventory.
        food_name: name of the food to add to the pantry.
    """
    nutrition = ask_nutritional_info()
    food = Food(food_name, nutrition)
    pantry.add_food(food)
    print(f"\nAdded to pantry:\n{food}")


def modify_food(pantry: Pantry, food: Food) -> None:
    food_name = food.name
    while True:
        print(f"\nModifying {food.name.title()}.")
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
                new_name = ask_food_name()
                if not new_name:
                    continue
                food.name = new_name
            case 2:
                serving_size = food.nutrition.serving_size
                print(f"\n{food.name} {serving_size}")
                try:
                    serving_size.amount = float(
                        input("Enter new serving size amount: ")
                    )
                except ValueError as e:
                    print(f"\n{e}")
                    continue
                serving_size.unit = input("Enter new serving size unit: ")
            case 3:
                print(f"\n{food.name} current proteins(g): {food.nutrition.proteins}")
                try:
                    food.nutrition.proteins = float(
                        input("Enter new protein(g) amount: ")
                    )
                except ValueError as e:
                    print(f"\n{e}")
            case 4:
                print(f"\n{food.name} current carbs(g): {food.nutrition.fats}")
                try:
                    food.nutrition.fats = float(input("Enter new fats(g) amount: "))
                except ValueError as e:
                    print(f"\n{e}")
            case 5:
                print(f"\n{food.name} current carbs(g): {food.nutrition.carbs}")
                try:
                    food.nutrition.carbs = float(input("Enter new carbs(g) amount: "))
                except ValueError as e:
                    print(f"\n{e}")
            case 6:
                food.nutrition = ask_nutritional_info()
            case 7:
                pantry.pop_food(food_name)
                pantry.add_food(food)
                return
            case _:
                print(f"Invalid option: {choice}")


def list_foods(pantry: Pantry) -> None:
    if not pantry.foods:
        print("\nYour pantry is empty. Try adding some foods!")
        return

    print("\nThis is your pantry:\n")
    print(pantry)


def remove_food(pantry: Pantry) -> None:
    food_name = input("Enter food name to be removed: ")
    food = pantry.pop_food(food_name)

    if not food:
        print(f"\n{food_name} wasn't found in pantry.")

    print(f"\nRemoved {food_name} from pantry.")


def prepare_meal(pantry: Pantry) -> None:
    if not pantry.foods:
        print("\nYour pantry is empty. Try adding some foods!")
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
        pantry_cp.pop_food(meal.name)


def route_request(request: int, pantry: Pantry) -> None:
    match request:
        case 1:
            list_foods(pantry)
        case 2:
            food_name = ask_food_name()
            food = pantry.get_food(food_name)
            if not food:
                add_food(pantry, food_name)
                return
            modify_food(pantry, food)
        case 3:
            remove_food(pantry)
        case 4:
            prepare_meal(pantry)
        case _:
            raise ValueError(f"invalid request: {request}")


def menu() -> None:
    print("\nFood Plan")
    print(SEPARATOR)
    print("1. Show food list.")
    print("2. Add or modify food.")
    print("3. Remove food.")
    print("4. Prepare a meal!")
    print("5. EXIT.")


def main():
    print("Welcome to Food Plan!")
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
