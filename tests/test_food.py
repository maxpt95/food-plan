from food import NutritionalInfo, ServingSize

TORTILLA_NUTRITION = {
    "serving_size": {"unit": "grams", "amount": 60},
    "fats": 4,
    "carbs": 27,
    "proteins": 6,
}


class TestNutritionalInfo:
    def test_from_dict(self):
        serving_size = ServingSize(**TORTILLA_NUTRITION["serving_size"])
        nutrition = NutritionalInfo(
            serving_size,
            fats=TORTILLA_NUTRITION["fats"],
            carbs=TORTILLA_NUTRITION["carbs"],
            proteins=TORTILLA_NUTRITION["proteins"],
        )
        assert nutrition == NutritionalInfo.from_dict(TORTILLA_NUTRITION)
