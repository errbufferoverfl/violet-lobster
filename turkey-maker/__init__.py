import logging
import math

import azure.functions as func

def isNumber(value_to_check: str) -> bool:
    try:
        float(value_to_check)
    except TypeError:
        return False
    else:
        return True

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    weight = req.params.get('weight')
    if not weight:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            weight = req_body.get('weight')

    if weight and isNumber(weight):
        weight = float(weight)
        brine_intructions = f"""Your turkey 🦃 weighs {weight} pounds, we'd recommend using the following:
🧂 {round(0.05 * weight, 1)} cups of salt
💦 {round(0.66 * weight, 2)} gallons of water
🍯 {round(0.13 * weight, 2)} cups of brown sugar
🧅 {round(0.2 * weight, 1)} shallots
🧄 {math.ceil(0.4 * weight)} cloves of garlic
⚫ {math.ceil(0.13 * weight)} tablespoons whole peppercorns
🍒 {math.ceil(0.13 * weight)} tablespoons dried juniper berries
🌿 {math.ceil(0.13 * weight)} tablespoons fresh rosemary
⏰ {math.ceil(0.06 * weight)} tablespoons thyme

🌊 Brine for {math.ceil(2.4 * weight)} hours
🍗 Roast for {math.ceil(15 * weight)} hours
        """

        return func.HttpResponse(brine_intructions)
    else:
        return func.HttpResponse(
             "Pass the weight of your turkey in pounds in the query string or in the request body for your brine equation.",
             status_code=200
        )
