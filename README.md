[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<br />
<p align="center">
  <a href="https://github.com/errbufferoverfl/violet-lobster">
    <img src="imgs/logo.png" alt="Logo" width="100" height="100">
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
  * [Solutions](#solutions)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)

## About the Project
<!-- ABOUT THE PROJECT -->

These are my soltutions to Microsoft's 2020 Seasons of Serverless challenges, each week I will attempt to write a solution using Python 3.8 and deploy it to Azure Functions. Each solution will be listed below, along with a screen capture.

### Solutions
<!-- SOLUTIONS -->

| Week | Challenge | Solution | Screen Capture | README |
|------|-----------|----------|----------------|--------|
| 1    | [The Perfect Holiday Turkey 🦃](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Nov-23-2020.md) | [Github Solution](https://github.com/errbufferoverfl/violet-lobster/tree/main/week-01) | <img src="imgs/turkey-recipe.PNG" alt="Image of Product" width="200"> | [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/week-01/README.md) |
| 2    | [Lovely Ladoos 💞](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Nov-30-2020.md) | [Detecting Lovely Ladoos Demo](https://stglovelyladoostest.z8.web.core.windows.net/) | <img src="imgs/lovely-ladoo.png" alt="Image of Product" width="200"> | [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/week-02/README.md) |
| 3    | [Longest Kebab 🥙](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Dec-7-2020.md) | [Flexitarian Demo](https://longest-kebab.azurewebsites.net/api/tartmak?type=flexitarian&weight=200) [Vegan Demo](https://longest-kebab.azurewebsites.net/api/tartmak?type=vegan&weight=200)  | <img src="imgs/longest-kebab.png" alt="Image of Product" width="200"> | [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/week-03/README.md) |
| 4    | [Biggest BBQ 🥩](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Dec-14-2020.md) | [Biggest BBQ Demo](https://big-bbq.azurewebsites.net/api/calcbudget?budget=99999)  | <img src="imgs/biggest-bbq.png" alt="Image of Product" width="200"> | [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/week-04/README.md) |

### Built With
<!-- BUILT WITH -->

* Azure Functions
* Azure Custom Vision
* Python 3.8

## Getting Started
<!-- GETTING STARTED -->

### Prerequisites
<!-- PREREQUISITES -->

* Microsoft Azure Account
* Python 3.8
* Each project comes with a `requirements.txt` that needs to be installed as part of deploying to Azure Functions.

### Installation
<!-- INSTALLATION -->

1. Clone the violet-lobster
```sh
git clone https://github.com/errbufferoverfl/violet-lobster.git
```
2. Create a virtual environment
```sh
cd violet-lobster/week-xx
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

Usage instructions can be found in each challenges' directory.
