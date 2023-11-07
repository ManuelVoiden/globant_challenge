from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pandas as pd
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
api = Api(app)

# Establish a connection to the database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('../db/test_prod.db')
        return conn
    except Error as e:
        print(e)
    return conn

# Define a resource for the hired_employees
class HiredEmployees(Resource):
    def get(self):
        conn = create_connection()
        df = pd.read_sql_query("SELECT * FROM hired_employees", conn)
        conn.close()
        return jsonify(df.to_dict(orient='records'))

    def post(self):
        conn = create_connection()
        # Assuming JSON request
        data = request.get_json()
        df = pd.DataFrame(data)
        df.to_sql('hired_employees', conn, if_exists='append', index=False)
        conn.commit()
        conn.close()
        return {'message': 'Data inserted successfully'}, 201

# Add the resource to the API
api.add_resource(HiredEmployees, '/hired_employees')

if __name__ == '__main__':
    app.run(debug=True)
