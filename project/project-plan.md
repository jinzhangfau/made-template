# Project Plan

## Title
<!-- Give your project a short title. -->
The influence of EUR/AUD currency exchange rate on Europeans' traveling to Australia.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
The exchange rate between different currencies is always fluctuating. Does the exchange rate influence traveling from a country to another?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Exchange rates can influence the purchasing power of a currency in terms of international trade or tourism. This project analyzes the exchange rate between euro (EUR) and Australian dollar (AUD), and the number of European tourist to Australia over a time period. The goal of this project is to find if there is any relationship between EUR/AUD exchange rate, and European citizen's travelling to Australia.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Australian Bureau of Statistics
* Data URL: https://explore.data.abs.gov.au/vis?tm=visitor%20arrivals&pg=0&df[ds]=ABS_ABS_TOPICS&df[id]=OAD_COUNTRY&df[ag]=ABS&df[vs]=1.0.0&pd=1999-01%2C2023-08&dq=...M&ly[cl]=TIME_PERIOD&ly[rw]=COUNTRY_RESID&ly[rs]=CAT_TRAVELLER
* Data Type: CSV
  
Excel sheet provided by the Australian Bureau of Statistics showing Visitor arrivals and resident returns from selected Countries of Residence/Destinations.

### Datasource2: European Central Bank
* Data URL: https://data.ecb.europa.eu/data/datasets/EXR/EXR.M.AUD.EUR.SP00.A
* Data Type: CSV

Excel sheet provided by the European Central Bank showing the exchange rate between euro and Australian dollar over time.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Datasources #1
2. Build an Automated Data Pipeline #2

[i1]: https://github.com/jvalue/made-template/issues/1
