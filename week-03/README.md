# Week 3 - Longest Kebab

## About the Challenge
<!-- ABOUT THE CHALLENGE -->

[Full Details](https://github.com/microsoft/Seasons-of-Serverless/blob/main/Dec-7-2020.md) | [Demo Site](https://longest-kebab.azurewebsites.net/api/tartmak?type=vegan&weight=200)

Adana kebabı or 'kebab' is a traditional meal, eaten in many religious and national holidays in Turkey. "It's a long, hand-minced meat kebab mounted on a wide iron skewer and grilled on an open mangal or grill filled with burning charcoal. The culinary item is named after Adana, the fifth largest city of Turkey" source. In the city of Adana, festivals are held with a competition centered around who can make the longest kebab in the world. At the festival, people have fun and eat this delicious dish!

## Tabel of Contents
<!-- TABLE OF CONTENTS -->

* [About the Challenge](#about-the-challenge)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)

## Usage
<!-- USAGE -->

Once you have followed the installation functions in the main [README](https://github.com/errbufferoverfl/violet-lobster/blob/main/README.md#installation) you can use the following instractions to use the longest kebab generation service:

1. Navigate to http://localhost:7071/api/tartmak

2. Append a query string using a browser or an API tool like Postman like so:
```sh
https://longest-kebab.azurewebsites.net/api/tartmak?type=vegan&weight=200
```

You should get the following response if your query was successful:
```
Turkish Style Vegan Kofte Kebabs

📚 https://www.connoisseurusveg.com/turkish-style-vegan-kofte-kebabs

Ingredients:
⚪ 200 kg chickpeas
🍞 502.0 cup panko breadcrumbs
🧅 502.0 onions coarsely chopped
🧄 1506.0 garlic cloves (minced)
🌰 502.0 tablespoon ground flaxseed
🌿 125.5 cup fresh parsley loosely packed
🟠 1004.0 teaspoons ground cumin
☘ 251.0 teaspoons ground coriander
🍠 251.0 teaspoons ground ginger
🔶 125.5 teaspoons ground cinnamon
🌶 a pinch cayenne pepper
🍶 753.0 tablespoon soy sauce
🍋 502.0 tablespoon lemon juice
🧂🌑 a pinch of salt and pepper (to taste)
🪔 1004.0 tablespoons olive oil

This recipe serves 2008.0 👨‍👨‍👦 people and could make 📏 0.24096 km (0.14973 miles) of kebab 😮.
```

This function has two types of recipe it can generate, `flexatarian` or `vegan`. This can be changed by specifying one of the two options in the `type=` query string.
