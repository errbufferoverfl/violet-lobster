<br />
<p align="center">
  <a href="https://github.com/errbufferoverfl/violet-lobster">
    <img src="imgs/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Violet Lobster</h3>

  <p align="center">
    Solutions to Microsoft's 2020 Seasons of Serverless challenges.
    <br />
    <a href="https://github.com/microsoft/Seasons-of-Serverless"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</p>

## Tabel of Contents
<!-- TABLE OF CONTENTS -->

* [About the Project](#about-the-project)
  * [Solutions]{#solutions}
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Expected Outputs](#expected-outputs)
* [Acknowledgements](#acknowledgements)

## About the Project
<!-- ABOUT THE PROJECT -->

These are my soltutions to Microsoft's 2020 Seasons of Serverless challenges, each week I will attempt to write a solution using Python 3.8 and deploy it to Azure Functions. Each solution will be listed below, along with a screen capture.

### Solutions
<!-- SOLUTIONS -->

| Week | Challenge | Solution | Screen Capture |
|------|-----------|----------|----------------|
| 1    | [Challenge 1: The Perfect Holiday Turkey 🦃](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Nov-23-2020.md) | | <img src="imgs/turkey-recipe.PNG" alt="Image of Product" width="100">

### Built With
<!-- BUILT WITH -->

* Azure Functions
* Python 3.8

## Getting Started
<!-- GETTING STARTED -->

### Prerequisites
<!-- PREREQUISITES -->

* Microsoft Azure Account
* Python 3.8

### Installation
<!-- INSTALLATION -->

1. Clone the violet-lobster
```sh
git clone https://github.com/errbufferoverfl/violet-lobster.git
```
2. Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate
```
3. Install the dependencies
```sh
pip install -r requirements.txt
```
4. Run the function locally
```sh
func start
```
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
Pass the weight of your turkey in pounds in the query string or in the request body for your brine equation.
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