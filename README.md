# MachineLearning-and-WebScraping-homes-in-Recife

Using webscraping to gather my own data to use in my machine learning model

# Purpose

The purpose of this project is mainly to learn more about Machine Learning and Web Scraping.

# Libraries used

when making this project, the libraries that I used Where:
- Selenium (WebScraping)
- Pandas (Data)
- Scikit-learn (MachineLearning)

# The Program

In the folder called "outras_amostras" I made the python files that accessed the website named "chaves na mao" to gather information about homes in Recife (Brazil) like size, location, number of bedrooms...

Using the .CSV files created during the WebScraping step, I made the Machine Learning Model that tries to predict de value of homes in Recife.

First using only the numeric data acquired (margin of error: about R$ 316.000,00)
- Size
- Number of bedrooms
- Number of bathrooms
- Number of parking spaces

then using all the data with OneHotEncoding (margin of error: about R$ 260.000,00)
- Location
- type of home (house, apartment, etc.)
- Size
- Number of bedrooms
- Number of bathrooms
- Number of parking spaces

The technique used in this project is Random Forest Regressor.
