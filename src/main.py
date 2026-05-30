"""Entry point of Food Plan

Where the user interface lives.
Most I/O operations should be concentrated here.
"""

import json
import time
from dataclasses import asdict

import config
from food import Food, NutritionalInfo, ServingSize
from pantry import Pantry


def add_food(pantry: Pantry):
    """Add food user interface.

    Adds a new food to pantry or overwrites
    an existing one.

    Args:
        pantry: the pantry instance to interact
        with the food inventory.
    """
    try:
        food = Food(input("Enter food name: ").lower())
    except ValueError as e:
        print(f"There was a problem adding your food: {e}")
        return

    if pantry.get_food(food) is not None:
        print(f"{food.name} already in Pantry.\n")
        print(food.nutrition)
        print("\nWould you like to modify it?")

        to_modify = input("Yes/No: ").lower()
        if to_modify == "no":
            return

    print("Insert food nutritional information.")
    serving_amount = input("Serving size amount: ")
    serving_unit = input("Serving size unit: ")
    fats = input("Fats (g): ")
    carbs = input("Carbs (g): ")
    proteins = input("Protein (g): ")

    serving = ServingSize(serving_amount, serving_unit)
    food.nutrition = NutritionalInfo(serving, fats, carbs, proteins)

    pantry.add_food(food)
    print(f"\nAdded to pantry: {food}")


def list_foods(pantry: Pantry) -> None:
    if not pantry.foods:
        print("\nYour pantry is empty. Try adding some foods!")
        return

    print("\nThis is your pantry:\n")
    print(pantry)


def remove_food(pantry: Pantry):
    raise NotImplementedError


def route_request(request: int, pantry: Pantry) -> None:
    match request:
        case 1:
            list_foods(pantry)
        case 2:
            add_food(pantry)
        case 3:
            remove_food(pantry)
        case 4:
            plan.generate_random_plate()
        case _:
            raise ValueError(f"invalid request: {request}")


def menu() -> None:
    print("\nFood Plan")
    print("----------------")
    print("1. Show food list.")
    print("2. Add or modify food.")
    print("3. Remove food.")
    print("4. Cook a random plate.")
    print("5. EXIT.")


def main():
    print("Welcome to Food Plan!")
    print("Loading pantry...")

    if not config.PANTRY_PATH.exists():
        config.PANTRY_PATH.write_text("{}", encoding="utf-8")

    pantry = Pantry(json.load(config.PANTRY_PATH.open()))
    while True:
        time.sleep(1)
        menu()
        try:
            request = int(input("\nChoose an option number: "))
        except ValueError:
            print("\nPlease choose one of the listed option numbers.")
            continue

        if request not in range(1, config.MENU_OPTIONS_NUMBER + 1):
            print(f"\n{request} isn't listed.")
            continue

        # chose to exit.
        if request == config.MENU_OPTIONS_NUMBER:
            with open(config.PANTRY_PATH, "w") as f:
                json.dump(asdict(pantry), f)

            return

        route_request(request, pantry)


if __name__ == "__main__":
    main()
