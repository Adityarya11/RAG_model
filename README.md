# RAG Model for QA Bot

## Overview
This project leverages **Ollama's Llama 3.1** in combination with a **custom stock and business data parser**, providing users with an intelligent chatbot capable of answering queries related to stock and business data. The system processes detailed stock information, such as 5-minute interval stock prices, turnover rates, and market share, alongside business insights like FAQs and company policies. By utilizing cutting-edge AI, the chatbot delivers accurate and actionable answers based on real-time and historical data.

---

## Features

- **Stock Query Capabilities:**
  - Identify the company with the highest turnover.
  - Analyze market share for specific companies at any time.
  - Monitor entry and exit rates of companies.
  - Extract 5-minute interval stock prices for all listed companies.

- **Business Insights:**
  - Retrieve detailed information about company policies, products, and services.
  - Quick answers to FAQs.

- **AI-Powered Intelligence:**
  - Powered by Llama 3.1 with 8B parameters for superior natural language understanding.
  - Seamless integration with parsed stock and business datasets for interactive querying.

---

## What is This Project?
This project integrates **Ollama's Llama 3.1**, a powerful language model, with parsed stock and business data to create an advanced Retrieval-Augmented Generation (RAG) model for QA purposes. 

### Data Flow and Components:
- **Models Folder:** Contains key Python scripts and assets that enable the RAG functionality.
- **Datasets:** Includes parsed company names and their respective stock data, retrieved from:
  - [Company Names Source](https://www.screener.in/screens/357649/all-listed-companies/)
  - [Stock Data Source](https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={Company_name}&interval=5min&apikey=demo&datatype=csv)

### Automated Data Retrieval:
- A Python script, powered by Selenium, scrapes company names from the first source.
- These names are then used to fetch detailed stock data (e.g., turnover, 5-minute stock prices) from the second source.
- The fetched data is upserted into the **Pinecone Database**, where:
  - Queries are transformed into vector encodings.
  - Top-k results are matched for optimal responses.

### User Interaction:
- **Backend:** Built with Django, managing the data processing and RAG logic.
- **Frontend:** A simple HTML, CSS, and JavaScript interface for smooth user interactions.

---

## Workflow

### High-Level Overview

1. **Data Input:**
    - Stock data files, containing 5-minute interval prices, are organized in a folder.
    - Business data is stored in a structured format.

2. **Query Processing:**
    - Users input queries (e.g., "Which company has the highest turnover?").
    - The system determines if the query pertains to stock or business data.

3. **Data Parsing:**
    - Stock files are analyzed to extract turnover, market share, and interval data.
    - Business data is parsed for textual insights.

4. **Response Generation:**
    - Parsed data is sent to Llama 3.1 for response generation.

5. **Output Delivery:**
    - Results are presented to users through the interface.

---

## Installation

### Prerequisites
- Python 3.8+
- Required libraries: `langchain_ollama`, `langchain_core`, `pandas`, `numpy`, `selenium`, `beautifulsoup4`

### Steps
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/stock-parser-llama.git
    cd stock-parser-llama
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Place stock files in the `data/stocks` folder.
4. Run the program:
    ```bash
    python app.py
    ```

---

## Code Explanation

### Core Logic

#### Query Processing
```python
from langchain_ollama import OllamaLLM
from scrape import get_stocks, business_data

model = OllamaLLM(model='Llama3.1')

def get_response(folder, business_data, question):
    response = model.get_response(question)
    return response
```
- **`folder`**: Contains stock files for each company.
- **`business_data`**: Includes preloaded business insights.
- **`get_response`**: Processes the user’s query and retrieves the response.

#### Parsing Stock Files
```python
import os
import pandas as pd

def get_stocks(folder):
    stocks = {}
    for file in os.listdir(folder):
        if file.endswith('.csv'):
            company_name = os.path.splitext(file)[0]
            stocks[company_name] = pd.read_csv(os.path.join(folder, file))
    return stocks
```
- **Reads all CSV files** in the specified folder.
- Maps each file to its respective company name for parsing.

---

## Example Queries

1. **Stock Queries:**
    - "Which company has the highest turnover?"
    - "Show me the 5-minute interval data for Company XYZ."

2. **Business Queries:**
    - "What’s the return policy?"
    - "Do you offer loyalty programs?"

---

## Workflow of the RAG Model

![Workflow Diagram](https://github.com/user-attachments/assets/4f34ff14-436d-43f9-bcc3-2c54039e27f6)

### Example Output
**Input:** "Which company has the highest turnover?"  
**Output:** "Company XYZ has the highest turnover of $5.2M as of the latest data."

---

## Contact
For questions or feedback, please reach out to [arya050411@gmail.com].

