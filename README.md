# Data Migration and Management API

This API is designed for data migration from CSV to a SQL database, managing data through RESTful endpoints, and providing backup and restore functionalities for the database tables.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.8 or later
- pip (Python package installer)
- Virtualenv (optional but recommended for creating a virtual environment)

### Installing

A step by step series of examples that tell you how to get a development environment running:

#### 1. Clone the repository

git clone <https://github.com/yourusername/globant_challenge.git>
cd globant_challenge

#### 1.1 (Optional) Create and activate a virtual environment

python -m venv venv
-On Windows
venv\Scripts\activate
-On Unix or MacOS
source venv/bin/activate

#### 2. Install the required packages

pip install -r requirements.txt

#### 3. Start the Flask development server

python api/main.py
The API will be available at <http://127.0.0.1:5000/>

#### 4. API endpoints

##### Get Data

GET /hired_employees - Retrieve all hired employees.
GET /departments - Retrieve all departments.
GET /jobs - Retrieve all jobs.

##### Post Data

POST /hired_employees - Add a new employee or a batch of employees. The request body should be a JSON object or an array of objects.
POST /departments - Add a new department or a batch of departments. The request body should be a JSON object or an array of objects.
POST /jobs - Add a new job or a batch of jobs. The request body should be a JSON object or an array of objects.

##### Backup and Restore

GET /backup/<table_name> - Create a backup of the specified table in AVRO format. The backup file will be named with the table name and the current date.
POST /restore/<table_name> - Restore the specified table from a backup. The request body should contain a JSON object with a date key indicating the date of the backup to restore from.

##### Backup and Restore Usage

###### To backup the hired_employees table

1. Send a GET request to <http://127.0.0.1:5000/backup/hired_employees>.
2. The backup file will be downloaded to your local machine.

###### To restore the hired_employees table from a backup

1. Send a POST request to <http://127.0.0.1:5000/restore/hired_employees> with a JSON body like
{"date": "YYYY-MM-DD"}
Replace YYYY-MM-DD with the date of the backup you wish to restore from.

#### 5. Challenge #2 endpoints

GET /metrics/employees-by-quarter - The response will be the table with the results, in alphabetical order in both the jobs and departments column
GET /metrics/departments-above-mean - The response will be the departments that hired more than the mean of employees hired by departments, its sorted in a descending way
