import pandas as pd
import numpy as np
import re

df = pd.read_csv('realistic_raw_scraped_data_no_emojis.csv')

df['sale_price'] = df['sale_price'].fillna(0)
df['rating'] = df['rating'].fillna(0)
df['brand'] = df['brand'].fillna('Unknown')
df['description'] = df['description'].fillna('No description provided')

df['market_price'] = df['market_price'].astype(str).str.replace('x', '', regex=False)
df['market_price'] = pd.to_numeric(df['market_price'], errors='coerce')
df['market_price'] = df['market_price'].fillna(0)

def clean_text(text):
    if not isinstance(text, str):
        return text
    text = ' '.join(text.strip().split())
    
    text = re.sub(r'[\!\?,\.\;\`\"()|&^#$%-*]+', '', text)
    
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r'', text)

df['product'] = df['product'].apply(clean_text)
df['category'] = df['category'].apply(clean_text).str.title()
df['sub_category'] = df['sub_category'].apply(clean_text).str.title()
df['brand'] = df['brand'].apply(clean_text)
df['type'] = df['type'].apply(clean_text)
df['description'] = df['description'].apply(clean_text)

print("Cleaned Data Info:")
print(df.info())
print("\nCleaned Data Head:")
print(df.head())

df.to_csv('cleaned_BigBasket_Products.csv', index=False)