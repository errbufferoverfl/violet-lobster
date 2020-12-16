# Week 4 - Biggest BBQ

## About the Challenge
<!-- ABOUT THE CHALLENGE -->

[Full Details](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Dec-14-2020.md) | [Demo Site](https://big-bbq.azurewebsites.net/api/calcbudget?budget=99999)

In Brazil, everyone loves a big barbecue! Brazilian barbecue is justifiably famous. Some families have created whole systems to help organize the amount of food needed for the number of people invited to a big barbecue. We have gained access to a spreadsheet used to organize large family barbecues: here it is. Big events like this can get expensive, and you need to stay in within your budget. Your challenge? Using the percentages in the spreadsheet, create a serverless method of determining how many people you can invite based on a given budget.

## Tabel of Contents
<!-- TABLE OF CONTENTS -->

* [About the Challenge](#about-the-challenge)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)

## Usage
<!-- USAGE -->

Once you have followed the installation functions in the main [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/README.md#installation) you can use the following instractions to use the longest kebab generation service:

1. Navigate to http://localhost:7071/api/calcbudget

2. Append a query string using a browser or an API tool like Postman like so:
```sh
https://big-bbq.azurewebsites.net/api/calcbudget?budget=99999
```

You should get the following response if your query was successful:
```
╒══════════════════╤════════════╕
│ Budget           │ $AUD 99999 │
├──────────────────┼────────────┤
│ # of People      │ 5872       │
├──────────────────┼────────────┤
│ Price Per Person │ $AUD 17.03 │
╘══════════════════╧════════════╛

╒════════════════╤════════════╕
│ Item           │   Qty (kg) │
╞════════════════╪════════════╡
│ chicken        │    1027.6  │
├────────────────┼────────────┤
│ beef           │     616.56 │
├────────────────┼────────────┤
│ fillet         │     616.56 │
├────────────────┼────────────┤
│ sausages       │     205.52 │
├────────────────┼────────────┤
│ halloumi       │     822.08 │
├────────────────┼────────────┤
│ garlic bread   │     205.52 │
├────────────────┼────────────┤
│ mushrooms      │     205.52 │
├────────────────┼────────────┤
│ fancy sausages │     205.52 │
├────────────────┼────────────┤
│ potatoes       │     205.52 │
╘════════════════╧════════════╛
```

This function has minimal error handling so try and stick to integers for now!
