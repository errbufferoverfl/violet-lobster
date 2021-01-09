import logging
import json
from pathlib import Path
import azure.functions as func

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    email = req.params.get('email')
    if not email:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            email = req_body.get('email')

    # region can be set to ghana | nigeria | senegal
    region = req.params.get('region').lower()
    if not region:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            region = req_body.get('region').lower()

    # there is an email address and a region specified
    if email and region:
        recipe = get_recipe(region)
        email_to_send = craft_email(email, recipe, region)
        sendGridMessage.set(json.dumps(email_to_send))

        return func.HttpResponse(f"Jollof recipe sent to {email}.")
    elif not email and region:
        recipe = get_recipe(region)
        return func.HttpResponse(recipe, mimetype="text/html")
    elif email and not region:
        return func.HttpResponse(f"Please specify a region (Ghana, Nigeria, or Senegal) to get a Jollof recipe.", status_code = 400)
    else:
        return func.HttpResponse(f"Please specify a region (Ghana, Nigeria, or Senegal) to get a Jollof recipe.", status_code = 400)

def get_recipe(region: str):
    if region in ["ghana", "nigeria", "senegal"]:
        recipe_path = Path.cwd() / "recipe-connector" / "recipes" / region
        with recipe_path.open() as file:
            value = file.read()
    return value
        

def craft_email(email_address: str, email_body: str, region: str):
    message = {
        "personalizations": [ {
            "to": [{"email": email_address
                }]}],
            "subject": f"Jollof Rice - {region}",
            "content": [{
                "type": "text/html",
                "value": email_body }]}

    return message