# Week 7 - The Recipe Connector

## About the Challenge
<!-- ABOUT THE CHALLENGE -->

[Full Details](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Jan-4-2021.md) | [Demo Site](https://big-bbq.azurewebsites.net/api/calcbudget?budget=99999)

In Africa, city cooks want to reconnect with their country roots. In Kenya, there are many traditional dishes, but no one in Nairobi remembers how to make them! In Lagos, Nigeria, cooks are eager to recreate their grandmother's famous jollof rice, but they can't quite remember the proportions of ingredients. Let's set up a City/Country hotline!

## Tabel of Contents
<!-- TABLE OF CONTENTS -->

* [About the Challenge](#about-the-challenge)
* [Usage](#usage)

## Usage
<!-- USAGE -->

Once you have followed the installation functions in the main [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/README.md#installation) you can use the following instructions to use the recipe connector service:

1. Navigate to http://localhost:7071/api/recipe-connector

2. Append a query string using a browser, or an API tool like Postman like so:
```
http://localhost:7071/api/recipe-connector?email=address@domain.com&region=nigeria
```
If you specified an email address as part of the query string, the recipe should be sent to you shortly.

You can also view the recipe locally if you don't want to supply your email, like so:
```
http://localhost:7071/api/recipe-connector?region=nigeria
```

**Note:** Currently you can specify Ghana, Nigeria, or Senegal to get a region specific Jollof recipe.

This function has minimal error handling so try to stick to integers for now!
