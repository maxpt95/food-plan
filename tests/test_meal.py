from copy import deepcopy

import pytest

from meal import NutritionalInfo, ServingSize


class TestServingSize:
    def test_equal(self, tortilla_serving: ServingSize):
        tortilla_serving_cp = deepcopy(tortilla_serving)

        assert tortilla_serving_cp == tortilla_serving

    def test_not_equal(self, tortilla_serving: ServingSize):
        tortilla_serving_cp = deepcopy(tortilla_serving)
        tortilla_serving_cp.amount = 999

        assert tortilla_serving_cp != tortilla_serving

    def test_init_negative_amount(self, tortilla_nutrition_dict: dict):
        tortilla_nutrition_dict["serving_size"]["amount"] *= -1

        with pytest.RaisesExc(ValueError, match="Amount can't be negative"):
            ServingSize(**tortilla_nutrition_dict["serving_size"])

    def test_set_negative_amount(self, tortilla_serving: ServingSize):
        with pytest.RaisesExc(ValueError, match="Amount can't be negative"):
            tortilla_serving.amount *= -1


class TestNutritionalInfo:
    def test_init_bad_macros(self, tortilla_nutrition_dict: dict):
        """Test macronutrients fail if negative"""

        tortilla_nutrition_dict["carbs"] *= -1
        with pytest.RaisesExc(ValueError):
            NutritionalInfo.from_dict(tortilla_nutrition_dict)

    def test_equal(self, tortilla_nutrition: NutritionalInfo):
        tortilla_nutrition_cp = deepcopy(tortilla_nutrition)

        assert tortilla_nutrition == tortilla_nutrition_cp, "tortillas should be equal "

    def test_not_equal(self, tortilla_nutrition: NutritionalInfo):
        tortilla_nutrition_cp = deepcopy(tortilla_nutrition)
        tortilla_nutrition_cp._fats = 999

        assert tortilla_nutrition_cp != tortilla_nutrition, (
            "tortillas shouldn't be equal"
        )

    def test_from_dict(self, tortilla_nutrition_dict: dict):
        serving_size = ServingSize(**tortilla_nutrition_dict["serving_size"])
        nutrition = NutritionalInfo(
            serving_size,
            fats=tortilla_nutrition_dict["fats"],
            carbs=tortilla_nutrition_dict["carbs"],
            proteins=tortilla_nutrition_dict["proteins"],
        )
        assert nutrition == NutritionalInfo.from_dict(tortilla_nutrition_dict)

    def test_set_negative_macrox(
        self, tortilla_nutrition: NutritionalInfo, subtests: pytest.Subtests
    ):
        for macro in ["fats", "carbs", "proteins"]:
            with subtests.test("setting negative a macro", macro=macro):
                with pytest.RaisesExc(ValueError, match=f"{macro} can't be negative"):
                    setattr(tortilla_nutrition, macro, -1)
