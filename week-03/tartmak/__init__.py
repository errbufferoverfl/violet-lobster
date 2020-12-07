import logging

import azure.functions as func

flexitarian_recipe = {
    "meat": 0.45359237,
    "onion": 1,
    "garlic": 4,
    "cumin": 1.5,
    "sumac": 1.5,
    "salt": 0.5,
    "pepper": 0.25, 
    "red pepper flakes": 0.25,
    "water": 2,
    "serves": 4,
    "makes": 48
}
vegan_recipe = {
    "chickpeas": 0.398,
    "panko breadcrumbs": 1,
    "onion": 1,
    "garlic": 3,
    "flaxseed": 1,
    "parsley": 0.25,
    "cumin": 2,
    "coriander": 0.5,
    "ginger": 0.5,
    "cinnamon": 0.25,
    "cayenne pepper": "a pinch",
    "soy sauce": 1.5,
    "lemon": 1,
    "salt and pepper": "a pinch",
    "oil": 2,
    "serves": 4,
    "makes": 48
}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    recipe_type = req.params.get('type')
    recipe_weight = req.params.get('weight')
    if not recipe_type:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            recipe_type = req_body.get('type')
            recipe_weight = req_body.get('weight')

    if recipe_type == 'flexitarian':
        multiplier = float(recipe_weight) // flexitarian_recipe["meat"]
        serving = flexitarian_recipe["serves"] * multiplier
        length_km = round(((flexitarian_recipe["makes"] * multiplier) / 100000), 5)
        length_mi = round((length_km * 0.621371), 5)

        return func.HttpResponse(f"""Adana Kebab (Ground Lamb Kebab)

📚 https://www.thespruceeats.com/adana-kebab-4164647

Ingredients:
🥩 {recipe_weight} kg minced lamb
🧅 {flexitarian_recipe["onion"] * multiplier} onions (minced)
🧄 {flexitarian_recipe["garlic"] * multiplier} garlic cloves (minced)
🟠 {flexitarian_recipe["cumin"] * multiplier} teaspoons ground cumin (divided)
🔴 {flexitarian_recipe["sumac"] * multiplier} teaspoons ground sumac (divided)
🧂 {flexitarian_recipe["salt"] * multiplier} teaspoon salt
🌑 {flexitarian_recipe["pepper"] * multiplier} teaspoon ground black pepper
🌶 {flexitarian_recipe["red pepper flakes"] * multiplier} teaspoon red pepper flakes (or to taste)
💧 {flexitarian_recipe["water"] * multiplier} tablespoons water (ice cold)

This recipe serves {serving} 👨‍👨‍👦 people and could make 📏 {length_km} km ({length_mi} miles) of kebab 😮.
""")

    elif recipe_type == 'vegan':
        multiplier = float(recipe_weight) // vegan_recipe["chickpeas"]
        serving = vegan_recipe["serves"] * multiplier
        length_km = round(((vegan_recipe["makes"] * multiplier) / 100000), 5)
        length_mi = round((length_km * 0.621371), 5)

        return func.HttpResponse(f"""Turkish Style Vegan Kofte Kebabs

📚 https://www.connoisseurusveg.com/turkish-style-vegan-kofte-kebabs

Ingredients:
⚪ {recipe_weight} kg chickpeas
🍞 {vegan_recipe["panko breadcrumbs"] * multiplier} cup panko breadcrumbs
🧅 {vegan_recipe["onion"] * multiplier} onions coarsely chopped
🧄 {vegan_recipe["garlic"] * multiplier} garlic cloves (minced)
🌰 {vegan_recipe["flaxseed"] * multiplier} tablespoon ground flaxseed
🌿 {vegan_recipe["parsley"] * multiplier} cup fresh parsley loosely packed
🟠 {vegan_recipe["cumin"] * multiplier} teaspoons ground cumin
☘ {vegan_recipe["coriander"] * multiplier} teaspoons ground coriander
🍠 {vegan_recipe["ginger"] * multiplier} teaspoons ground ginger
🔶 {vegan_recipe["cinnamon"] * multiplier} teaspoons ground cinnamon
🌶 a pinch cayenne pepper
🍶 {vegan_recipe["soy sauce"] * multiplier} tablespoon soy sauce
🍋 {vegan_recipe["lemon"] * multiplier} tablespoon lemon juice
🧂🌑 a pinch of salt and pepper (to taste)
🪔 {vegan_recipe["oil"] * multiplier} tablespoons olive oil

This recipe serves {serving} 👨‍👨‍👦 people and could make 📏 {length_km} km ({length_mi} miles) of kebab 😮.
""")

    else:
        return func.HttpResponse("""ABOUT
=======

This is an Azure Function with an HTTP Trigger! If you're seeing this page it means that the function triggered successfully, but you provided no input. No worries though, 
below are some instructions on how you can get started.

HELP!
======

To get started, append a query string using a browser or an API tool like Postmap like so:

http://localhost:7071/api/tartmak?type=vegan&weight=1000

You can also request a "flexatarian" recipe by changing the type to flexatarian like so:

http://localhost:7071/api/tartmak?type=flexatarian&weight=1000

"""
)
