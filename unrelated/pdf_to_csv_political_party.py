import fitz
import pandas as pd
import csv

doc = fitz.open("political_party.pdf")

concatThis = []
for i in range(len(doc)):
    page = doc[i]
    tables = page.find_tables()
    table = tables[0]
    pagedata = table.to_pandas()
    concatThis.append(pagedata)

main = pd.concat(concatThis)

main.rename(columns={"Date of\nEncashment": "Date of Encashment", "Account no. of\nPolitical Party": "Account no. of Political Party", "Bond\nNumber":"Bond Number", "Pay Branch\nCode":"Pay Branch Code"}, inplace=True)



main.to_csv('political_party_csv.csv', index=False)