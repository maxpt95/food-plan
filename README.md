# Meal Prep

Meal Prep is a CLI application to help you resize your meals to fit your calory budget.

## Features

- [Add, modify or remove](#adding-modifying-and-removing-meals) meals from your [fridge](#the-fridge).
- [Show all the meals](#look-at-your-fridge) in your fridge with their macronutrients.
- [Meal prep](#meal-prepping) a random meal: resize a random meal from your fridge.
- Meal prep a given meal: resize a specific meal from your fridge.


## Getting Started

### Requirements
- [Python 3.13 or later](https://www.python.org/downloads/)

### Installation

1. Clone Meal Prep repo
```sh
git clone https://github.com/maxpt95/meal-prep.git
cd meal-prep
```
2. Start Meal Prep with `./run.sh`

## Using Meal prep

### The Fridge

The **fridge** is the place where all your added meals live. You'll find an example
fridge in the `fridge_example.json`. If you want to use it just rename it to `fridge.json`,
if not simply start up Meal Prep and it will create a clean one of your own!

### Adding, modifying and removing meals.

You may add or modify meals by selecting *Add or modify meal*. When prompted to enter a meal name:

- Entering a meal not in your fridge will create a new one.
- Entering a meal that exists in your fridge will modify the existing one.

You may remove a meal by selecting *Remove meal*.

Your fridge will be **saved on exit**.

### Look at Your Fridge

By selecting *Show meal list* Meal Prep will show you
a complete list of the meals in your fridge with their
macronutrient summary.

### Meal Prepping

Choose *Prep a meal!* from the Main Menu, and Meal Prep will
prompt you to enter a meal name and calory budget. Meal Prep
then will look for that meal in your fridge and resize the serving
for it to fit your given calorie budget.

## License

[MIT](https://choosealicense.com/licenses/mit/)

# What's cooking!

- [ ] store recipe urls in meals!
