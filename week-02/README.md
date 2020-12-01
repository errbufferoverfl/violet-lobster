# Week 2 - Lovely Ladoo

## About the Challenge
<!-- ABOUT THE CHALLENGE -->

[Full Details](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Nov-30-2020.md) | [Demo Site](https://stglovelyladoostest.z8.web.core.windows.net/)

It's Diwali season in India! Diwali is a festival that celebrates the victory of light over darkness. Families celebrate with fireworks and light up every house in the country with diyas, a type of Indian candles. A very popular delicacy that Indians eat during Diwali is ladoos.

Ladoos are balls of flour dipped in sugar syrup. Since we're in the middle of a global pandemic, most of the celebrations have to be done from home and we have to be innovative to find our inner child to have fun during Diwali 2020. Thanks to technology, however, we're still connected to our loved ones virtually!

## Tabel of Contents
<!-- TABLE OF CONTENTS -->

* [About the Challenge](#about-the-challenge)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)

## Usage
<!-- USAGE -->

Once you have followed the installation functions in the main [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/README.md#installation) you can use the following instractions to use the lovely ladoos classification service:

1. Navigate to http://localhost:7071/api/classify

2. Append a query string using a browser or an API tool like Postman like so:
```sh
http://localhost:7071/api/classify?img=ihttps://upload.wikimedia.org/wikipedia/commons/0/04/New_York_Empire_Apples.jpg
```

You should get the following response if your query was successful:
```
{"created": "2020-12-01T02:07:42.286272", "predictedTagName": "gulab jamun", "prediction": [{"tagName": "doughnut hole", "probability": 1.8930000805994496e-05}, {"tagName": "gulab jamun", "probability": 0.99713134765625}, {"tagName": "ladoo", "probability": 0.002848200034350157}, {"tagName": "Negative", "probability": 6.099999723119254e-07}, {"tagName": "truffles", "probability": 9.19999990856013e-07}]}
```

This JSON response can then be consumed using Azure storage account (with static website hosting enabled) and processed using JavaScript.

## Acknowledgements

* [Tutorial: Apply machine learning models in Azure Functions with Python and TensorFlow](https://docs.microsoft.com/en-us/azure/azure-functions/functions-machine-learning-tensorflow)