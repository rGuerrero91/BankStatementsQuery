import re
import pdfplumber
import pandas as pd
import os
# pdf_path = "./statements/20240308-statements-6793-.pdf"
def clean_amount(amount):
    amount = amount.replace(",", "") 
    return float(amount)

def extract_table_from_statement(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    transaction_pattern = re.compile(
        r"(\d{2}/\d{2})\s+(.+?)\s+([+-]?\(?\d{1,3}(?:,\d{3})*(?:\.\d{2})?\)?)\s+(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)"
    )

    transactions = transaction_pattern.findall(text)

    cleaned_transactions = []
    for date, desc, amount, balance in transactions:
        cleaned_transactions.append((date, desc.strip(), clean_amount(amount), clean_amount(balance)))

    return cleaned_transactions

transactions = []

directory = "./statements"
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        transactions += extract_table_from_statement(os.path.join(directory, filename))

df = pd.DataFrame(transactions, columns=["Date", "Description", "Amount", "Balance"])

# df.to_csv("./output.csv")
df.to_excel("./output.xlsx", sheet_name='Transactions', index=False)

# print(df)
# return df