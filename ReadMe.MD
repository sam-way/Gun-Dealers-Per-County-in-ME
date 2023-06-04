# 2023 List of Maine Gun Dealers

This repository generates a county-wise list of gun dealers in Maine, by scraping and processing data from various sources. It also visualizes the data by creating a bar graph depicting the number of dealers per county.

Source Data URL: https://www.fflregistry.com/FFL-Dealers-Location/Maine-ME

Requirements

    Python 3.x
    Beautiful Soup
    Pandas
    Matplotlib
    Requests

Usage

Step 1: Get Town and County data from Wikipedia. Run the following script to scrape this data and save it as a CSV file.

```
python src/wikiscrape.py
```
Step 2: Process raw data, map each dealer to a county, generate a bar graph of dealers per county, and save the processed data into a CSV file.

```
python src/editAndCombine.py
```

<img src="Bar Graph of Gun Dealers.png" width=500>

Note: Run the scripts in the order mentioned above. Inconsistencies in source data may lead to some missing or misplaced names and addresses.

Contributing: Pull requests are welcome. For major changes, open an issue first to discuss proposed modifications.

License: This project is licensed under the terms of the MIT license.
