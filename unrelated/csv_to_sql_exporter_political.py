import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SapphirE IS_liT27",
    database="dcc_a4"
)

cursor = mydb.cursor()

with open('political_party_csv.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row (if present)
    for row in reader:
        insert_query = """
            INSERT INTO political_bonds (
                Sr_No, 
                Date_of_Encashment, 
                Name_of_the_Political_Party, 
                Account_no_of_Political_Party, 
                Prefix, 
                Bond_Number, 
                Denominations, 
                Pay_Branch_Code, 
                Pay_Teller
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
        """
        values = tuple(row)
        cursor.execute(insert_query, values)

mydb.commit()
cursor.close()
mydb.close()