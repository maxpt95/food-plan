"""Entry point of Food Plan

Where the user interface lives.
Most I/O operations should be concentrated here.
"""

import time

import pantry
import plan
from food import Food, NutritionalInfo


def add_food():
    """Add food user interface.

    Adds a new food to pantry or overwrites
    an existing one.
    """
    try:
        food = Food(input("Enter food name: "))
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
    fats = input("Fats (g): ")
    carbs = input("Carbs (g): ")
    proteins = input("Protein (g): ")

    food.nutrition = NutritionalInfo(fats, carbs, proteins)
    pantry.add_food(food)


def route_request(request: int) -> None:
    match request:
        case 1:
            add_food()
        case 2:
            pantry.list_foods()
        case 3:
            plan.generate_random_plate()
        case _:
            raise ValueError(f"invalid request: {request}")


def menu() -> None:
    print("\nFood Plan")
    print("----------------")
    print("1. Add new food.")
    print("2. Show food list.")
    print("3. Cook a random plate.")
    print("4. EXIT.")


def main():
    print("Welcome to Food Plan!")

    while True:
        time.sleep(0.5)
        menu()
        try:
            request = int(input("\nChoose an option number: "))
        except ValueError:
            print("\nPlease choose one of the listed option numbers.")
            continue

        if request not in range(1, 5):
            print(f"\n{request} isn't listed.")
            continue

        # chose to exit.
        if request == 4:
            return

        route_request(request)


if __name__ == "__main__":
    main()
