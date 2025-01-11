from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from scrape import get_stocks, business_data
import os 
import pandas as pd

model = OllamaLLM(model='Llama3.1')

def parse_stockfolder(folderpath):
    all_data = []
    for filename in os.listdir(folderpath):
        if filename.endswith('.csv'):
            file_path = os.path.join(folderpath, filename)
            
            try:
                df = pd.read_csv(file_path)
                df['company'] = filename.replace("_stocks.csv", "")
                all_data.append(df)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    
    combined_data = pd.concat(all_data, ignore_index=True)
    return combined_data

# Now accepts the question parameter properly
def get_response(stock_folder, business_data, question):
    stock_data = parse_stockfolder(stock_folder)
    
    # Displaying only a small sample of stock data for context
    stock_info = stock_data.head().to_string()
    
    # Creating the context for the LLM
    context = "\n\n".join(business_data) + "\n\nStock Data (sample):\n" + stock_info
    prompt = ChatPromptTemplate.from_template("{question}\n\n{parse_desc}")
    parsed_result = []
    
    # Sending the user question to the model
    chain = prompt | model
    response = chain.invoke({"question": question, "parse_desc": context})
    
    return response

# This function will be called from views.py
def process_question(question):
    stock_folder = "./files"  
    response = get_response(stock_folder, business_data, question)
    return response
