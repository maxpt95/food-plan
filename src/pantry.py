from food import Food


class Pantry:
    def __init__(self, pantry: dict):
        self.pantry = pantry

    def add_food(food: Food):
        raise NotImplementedError

    def get_food(self, food: Food) -> Food | None:
        return self.pantry.get(food.name)

    def list_foods(pantry):
        raise NotImplementedError
