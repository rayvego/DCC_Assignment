import fitz
import pandas as pd
import csv

doc = fitz.open("ind_and_comp.pdf")

concatThis = []
for i in range(len(doc)):
    page = doc[i]
    tables = page.find_tables()
    table = tables[0]
    pagedata = table.to_pandas()
    concatThis.append(pagedata)

main = pd.concat(concatThis)
pd.set_option('display.max_columns', None)
main.rename(columns={"Date of\nPurchase": "Date of Purchase", "Bond\nNumber": "Bond Number"}, inplace=True)

main.to_csv('ind_and_comp_csv.csv', index=False)