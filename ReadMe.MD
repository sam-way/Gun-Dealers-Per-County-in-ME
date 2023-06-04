# 2023 List of Maine Gun Dealers

This is a project that generates a list of Maine gun dealers broken down by county. 
It scrapes a list of towns and corresponding counties from Wikipedia.
Process the raw data to map each gun dealer to a county and generate a bar graph of the number of dealers per county.

URL of the Source Data
url =https://www.fflregistry.com/FFL-Dealers-Location/Maine-ME

Requirements

    Python 3.x
    Beautiful Soup
    Pandas
    Matplotlib
    requests

Usage

Step 1: Scrape Town and County data from Wikipedia

Before generating the list of gun dealers, we need to get a list of towns and corresponding counties. The following Python script scrapes this data from Wikipedia and saves it as a CSV file.

Step 2: Generate the List of Gun Dealers

This script reads the input data, processes it, maps each dealer to a county, generates a bar graph of the number of dealers per county, and finally saves the processed data into a CSV file.

<img src="Bar Graph of Gun Dealers.png" width=500>

Note: Both scripts must be run in the mentioned order for the correct generation of the gun dealers list. Due to inconsistencies in the source data some of the names and address are missing or in the wrong place.

Contributing: Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License: MIT