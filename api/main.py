import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from src.models.schemas import EmployeeModel, DepartmentModel, JobModel
import pandas as pd
import sqlite3
from sqlite3 import Error
import pydantic
from pydantic import ValidationError

app = Flask(__name__)
api = Api(app)

# Establish a connection to the database
def create_connection():
    conn = None
    base_dir = os.path.abspath(os.path.dirname(__file__))  # Absolute path to the api folder
    database_path = os.path.join(base_dir, '../db/test_prod.db')  # Corrected path to the db folder
    try:
        conn = sqlite3.connect(database_path)
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
        
        data = request.get_json()
        
        if isinstance(data, dict):
            data = [data]  # Now `data` is a list with one dict
        
        # Ensure that data is a list of records
        if not isinstance(data, list):
            return {'message': 'Input data should be a list of records'}, 400
        
        # Check if the batch size is within the limit
        if len(data) > 1000:
            return {'message': 'Batch size exceeds the limit of 1000 rows'}, 400

        try:
            # Start a transaction
            with conn:
                # Validate and insert each record in the batch
                for item in data:
                    validated_item = EmployeeModel(**item)
                    df = pd.DataFrame([validated_item.dict()])
                    df.to_sql('hired_employees', conn, if_exists='append', index=False)
            
            return {'message': 'Batch data inserted successfully'}, 201

        except ValidationError as e:
            return {'message': 'Validation error', 'errors': e.errors()}, 400
        except Error as e:
            return {'message': 'Database error', 'errors': str(e)}, 500
        finally:
            conn.close()


class Departments(Resource):
    def get(self):
        conn = create_connection()
        df = pd.read_sql_query("SELECT * FROM departments", conn)
        conn.close()
        return jsonify(df.to_dict(orient='records'))

    def post(self):
        conn = create_connection()
        # Assuming JSON request
        data = request.get_json()
        
        try:
            # Validate data against the schema
            validated_data = [DepartmentModel(**item) for item in data]
            # Convert validated data back to list of dicts
            insert_data = [item.dict() for item in validated_data]
            
            # Insert validated and transformed data into the database
            df = pd.DataFrame(insert_data)
            df.to_sql('departments', conn, if_exists='append', index=False)
            conn.commit()
            conn.close()
            return {'message': 'Data inserted successfully'}, 201
        except ValidationError as e:
            conn.close()
            return {'message': 'Validation error', 'errors': e.errors()}, 400

class Jobs(Resource):
    def get(self):
        conn = create_connection()
        df = pd.read_sql_query("SELECT * FROM jobs", conn)
        conn.close()
        return jsonify(df.to_dict(orient='records'))

    def post(self):
        conn = create_connection()
        # Assuming JSON request
        data = request.get_json()
        
        try:
            # Validate data against the schema
            validated_data = [JobModel(**item) for item in data]
            # Convert validated data back to list of dicts
            insert_data = [item.dict() for item in validated_data]
            
            df = pd.DataFrame(insert_data)
            df.to_sql('jobs', conn, if_exists='append', index=False)
            conn.commit()
            conn.close()
            return {'message': 'Data inserted successfully'}, 201
        except ValidationError as e:
            conn.close()
            return {'message': 'Validation error', 'errors': e.errors()}, 400

# Add the resource to the API
api.add_resource(HiredEmployees, '/hired_employees')
api.add_resource(Departments, '/departments')
api.add_resource(Jobs, '/jobs')

if __name__ == '__main__':
    app.run(debug=True)
