import re
import pdfplumber
import pandas as pd

# pdf_path = "./statements/20240308-statements-6793-.pdf"

def extract_table_from_statement(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Regex for transaction lines
    transaction_pattern = re.compile(r"(\d{2}/\d{2})\s+(.*?)\s+([+-]?\d+\.\d{2})\s+(\d+\.\d{2})")
    transactions = transaction_pattern.findall(text)


    # text = """
    # Bank Statement
    # Account Number: 123456789
    # Statement Period: 01/01/2023 - 01/31/2023

    # Date       Description              Amount
    # 01/02/2023 Grocery Store            -50.00
    # 01/05/2023 Salary Deposit          +2000.00
    # 01/10/2023 Online Shopping         -100.00
    # 01/15/2023 ATM Withdrawal          -200.00

    # Total Balance: 1650.00
    # """

    # Array of transactions to DataFrame (tables)
    df = pd.DataFrame(transactions, columns=["Date", "Description", "Amount", "Balance"])
    df["Amount"] = df["Amount"].astype(float)
    df["Balance"] = df["Balance"].astype(float)
    return df





import os
directory = os.fsencode("./statements")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        # print(os.path.join(filename))
        continue
    else:
        continue
      