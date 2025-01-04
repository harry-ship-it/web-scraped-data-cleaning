import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup

# Load the dataset
data = pd.read_csv('raw_web_data.csv')

print("Original Data:")
print(data.head())

# Step 1: Remove HTML Tags from Product Names
def clean_html(text):
    return BeautifulSoup(text, "html.parser").get_text()

data['product_name'] = data['product_name'].apply(clean_html)

# Step 2: Convert Prices to Numeric Values
data['price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)

# Step 3: Handle Missing Values
# Fill missing prices with median price
data['price'] = data['price'].fillna(data['price'].median())

# Fill missing ratings with mode
data['rating'] = data['rating'].fillna(data['rating'].mode()[0])

# Step 4: Standardize Date Formats
data['date_scraped'] = pd.to_datetime(data['date_scraped'], errors='coerce')

# Step 5: Remove Duplicates
data = data.drop_duplicates()

# Step 6: Save Cleaned Data
cleaned_file_path = 'cleaned_web_data.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
