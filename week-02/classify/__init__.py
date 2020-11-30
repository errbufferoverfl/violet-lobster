import logging

import azure.functions as func
from .predict import predict_image_from_url
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    headers = { "Content-type": "application/json",}

    image_url = req.params.get('img')

    if not image_url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            image_url = req_body.get('image_url')

    if image_url:
        results = predict_image_from_url(image_url)

        return func.HttpResponse(json.dumps(results), headers=headers)