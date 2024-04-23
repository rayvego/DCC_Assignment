import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SapphirE IS_liT27",
    database="dcc_a4"
)

cursor = mydb.cursor()

with open('ind_and_comp_csv.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row (if present)
    for row in reader:
        insert_query = """
            INSERT INTO ind_and_comp_bonds (
            Sr_No,
            Reference_No,
            Journal_Date,
            Date_of_Purchase,
            Date_of_Expiry,
            Name_of_the_Purchaser,
            Prefix,
            Bond_Number,
            Denominations,
            Issue_Branch_Code,
            Issue_Teller,
            Status
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = tuple(row)
        cursor.execute(insert_query, values)

mydb.commit()
cursor.close()
mydb.close()