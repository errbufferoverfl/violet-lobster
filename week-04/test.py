import logging

import azure.functions as func


from math import floor

# defines the price of food per kilo (or as close to as possible)
# TODO combine the prices and percentages into one dict
from tabulate import tabulate

prices = {
    "chicken": 15.00,
    "beef": 30.00,
    "fillet": 45.50,
    "sausages": 15.00,
    "halloumi": 30.00,
    "garlic bread": 10.00,
    "mushrooms": 10.00,
    "fancy sausages": 20.00,
    "potatoes": 10.00
}

# defines plate composition in percentages
# this dictionary is used to allocate the estimated_weight_eaten
percentages = {
    "chicken": 25,
    "beef": 15,
    "fillet": 15,
    "sausages": 5,
    "halloumi": 20,
    "garlic bread": 5,
    "mushrooms": 5,
    "fancy sausages": 5,
    "potatoes": 5
}


def calc_price_per_person(qnt_per_person: dict) -> float:
    """
    Calculates based on the plate composition how much a plate of food costs per person. This is done by taking the
    amount in kilograms (e.g. .134) and multiplying it by the price per kilo (`prices` dict)

    Args:
        qnt_per_person: dict containing the weight of each type of food (reflected in kilograms) in the percentages
        dictionary.

    Returns: float that represents price per person

    """
    total_sum = list()

    for key in qnt_per_person:
        total_sum.append(qnt_per_person[key] * prices[key])

    return sum(total_sum)


def percentage(percent: float, whole: float) -> int:
    """
    Calculates the percentage that a value makes up, i.e. 20% of 8 = 1.6
    Args:
        percent: float reflecting the percentage you want to find
        whole: float reflecting the total value of the thing you're trying to find the percentage of

    Returns:
        int that is the percentage of the whole

    """
    return (percent * whole) / 100.0


def calculate_shopping_list() -> dict:
    estimated_weight_eaten = 0.700
    food_per_person = dict()
    for key in percentages:
        food_per_person[key] = percentage(percentages[key], estimated_weight_eaten)

    return food_per_person


def calculate_people(budget: int) -> int:
    """
    Calculates the number of people you can order based on a specified budget. This is based on:
    1. Define how much you estimate people will eat using the `estimated_weight_eaten` value (reflected in kgs)
    2. For each food item listed in price (and percentage) calculate how much people will eat, based on the percentage
        defined in the percentages dict
    3. Calculate the price per person
    4. Divide the total budget by the price per person
    5. Floor this value so we don't spend too much

    Args:
        budget: int - total amount of money we are willing to spend at our BBQ

    Returns:
        int - the number of people you can serve at your BBQ

    """
    shopping_list = calculate_shopping_list()
    ppp = calc_price_per_person(shopping_list)
    people_u_can_serve = budget / ppp

    people_u_can_serve = floor(people_u_can_serve)

    return people_u_can_serve


def build_shopping_list(shopping_list: dict, people: int):
    shopping_list_headers = ["Item", "Qty (kg)"]
    shopping_list_values = list()

    for key in shopping_list:
        shopping_list_values.append([key, round(shopping_list[key] * people, 2)])

    return tabulate(shopping_list_values, shopping_list_headers, tablefmt="fancy_grid")


def main():
    budget = 900

    if budget and int(budget):
        budget = int(budget)
        people = calculate_people(budget)
        shopping_list = calculate_shopping_list()

        styled_budget = list()
        styled_budget.append(["Budget", f"$AUD {budget}"])
        styled_budget.append(["# of People", people])
        styled_budget.append(["Price Per Person", f"$AUD {round(calc_price_per_person(shopping_list), 2)}"])

        print(build_shopping_list(shopping_list, people))
        print(tabulate(styled_budget, tablefmt="fancy_grid"))


main()