from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

# setting up mysql connector
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SapphirE IS_liT27'
app.config['MYSQL_DB'] = 'dcc_a4'


@app.route('/political_bonds', methods=["GET", "POST"])
def political_bonds():
    if request.method == "GET":
        mydb = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )

        cursor = mydb.cursor()
        query = "SELECT * FROM political_bonds"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        print(type(data))
        return render_template('political_bonds.html', data=data)
    elif request.method == "POST":
        query = request.form.get('query')
        print("Search Query:", query)  # Print to console

        results = search_database(query)
        print(results)
        return render_template('political_bonds.html', query=query, data=results)


def search_database(query):
    mydb = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    cursor = mydb.cursor()

    # Parameterized query for safety
    sql_query = "SELECT * FROM political_bonds WHERE Bond_Number LIKE %s"
    search_term = '%' + query + '%'

    cursor.execute(sql_query, (search_term,))  # Pass search_term as a tuple
    results = cursor.fetchall()
    cursor.close()
    mydb.close()
    return results


@app.route("/individual_and_companies", methods=["GET"])
def individual_and_companies():
    return render_template("ind_and_comp.html")


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/get_data', methods=['GET'])
def get_data():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM political_bonds')
    data = cursor.fetchall()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
