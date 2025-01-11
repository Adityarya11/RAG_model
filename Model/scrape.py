# This file is for scraping the data from the websites such as Company names and their respective Stocks.

import os
import requests
from bs4 import BeautifulSoup

def get_company_names():
    output_file = "company_names.txt"

    base_url = "https://www.screener.in/screens/357649/all-listed-companies/?page={}&&limit=50"

    with open(output_file, "w") as file:
        for i in range(1, 196):
            print(f"Fetching page {i}...")
            url = base_url.format(i)
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")


                rows = soup.select('table.data-table tbody tr')

                for row in rows:

                    name_cell = row.select_one('td.text a')
                    if name_cell:
                        company_name = name_cell.text.strip()
                        file.write(company_name + "\n")
            else:
                print(f"Failed to fetch page {i}. Status code: {response.status_code}")
    print(f"Company names have been saved to {output_file}.")


def get_stocks():

    API_KEY = ''  #free api key

    company_file = 'company_names.txt'


    output_dir = 'Stocks'
    os.makedirs(output_dir, exist_ok=True)


    with open(company_file, 'r') as file:
        company_names = [line.strip() for line in file.readlines()]


    for company_name in company_names:
        print(f"Fetching data for {company_name}...")
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=Milkfood&interval=5min&apikey={API_KEY}&datatype=csv'
        response = requests.get(url)


        if response.status_code == 200:
            csv_data = response.text
            file_path = os.path.join(output_dir, f"{company_name}_stocks.csv")
            with open(file_path, 'w') as csv_file:
                csv_file.write(csv_data)
            print(f"Data saved for {company_name} in {file_path}")
        else:
            print(f"Failed to fetch data for {company_name}. Status Code: {response.status_code}")

    print("Stock data fetching completed!")


## Some basics FAQs for the bot to answer.
business_data = [
    #General Stock Queries:
    "Which company has the highest market turnover this month?",
    "List companies with the highest market capitalization.",
    "Which company had the highest stock value fluctuation in the last week?",

    #Company-Specific Queries:
    "What is the current market share of [Company Name]?",
    "What was the entry price of [Company Name] on [Date]?",
    "What was the exit rate for [Company Name] during the last quarter?",
    #Time-Based Queries:
    "Provide the 5-minute interval stock value for [Company Name] on [Date].",
    "What was the highest stock price for [Company Name] between 10 AM and 2 PM yesterday?",
    "Compare the stock prices of [Company A] and [Company B] in the last 24 hours.",
    #Financial Performance Queries:
    "Which company showed the highest profit margin last year?",
    "List the companies with declining market share over the past quarter.",
    "Provide the dividend payout history of [Company Name]."
]

get_company_names()
get_stocks()