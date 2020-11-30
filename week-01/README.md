# Week 1 - The Perfect Turkey

## Usage
<!-- USAGE -->

1. Navigate to http://localhost:7071/api/turkey-maker

2. Append a query string using a browser or an API tool like Postmap like so:
```sh
http://localhost:7071/api/turkey-maker?weight=20
```
You should get the following response if your query was successful:
```
Your turkey 🦃 weighs 20.0 pounds, we'd recommend using the following:
🧂 1.0 cups of salt
💦 13.2 gallons of water
🍯 2.6 cups of brown sugar
🧅 4.0 shallots
🧄 8 cloves of garlic
⚫ 3 tablespoons whole peppercorns
🍒 3 tablespoons dried juniper berries
🌿 3 tablespoons fresh rosemary
⏰ 2 tablespoons thyme

🌊 Brine for 48 hours
🍗 Roast for 300 minutes
```

### Expected Outputs

Below I will provide some examples of invalid input and the expected outcomes, this is a proof of concept so the API does still return 200 when there is a problem.

✔ **Valid**

Input:
```sh
http://localhost:7071/api/turkey-maker?weight=20
```

Expected Output:
```
Your turkey 🦃 weighs 20.0 pounds, we'd recommend using the following:
🧂 1.0 cups of salt
💦 13.2 gallons of water
🍯 2.6 cups of brown sugar
🧅 4.0 shallots
🧄 8 cloves of garlic
⚫ 3 tablespoons whole peppercorns
🍒 3 tablespoons dried juniper berries
🌿 3 tablespoons fresh rosemary
⏰ 2 tablespoons thyme

🌊 Brine for 48 hours
🍗 Roast for 300 minutes
```

✔ **Valid (but boring)**

Input:
```sh
http://localhost:7071/api/turkey-maker
```

Expected Output:
```
Pass the weight of your turkey in pounds in the query string or in the request body for your brine equation.
```

❌ **Invalid**

Input:
```sh
http://localhost:7071/api/turkey-maker?notawight=20
```

Expected Output:
```
Pass the weight of your turkey in pounds in the query string or in the request body for your brine equation.
```

❌ **Invalid**

Input:
```sh
http://localhost:7071/api/turkey-maker?weight=aaaa
```

Expected Output:
```
Pass the weight of your turkey in pounds in the query string or in the request body for your brine equation.
```
