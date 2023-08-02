# Footballers-flask-api

This project contains an API that was created using the Flask framework for Python.
The API allows you to manage a postgreSQL database using ElephantSQL, that contains data on football players.

[Deployed version](https://footballers-flask-api.onrender.com/footballers)

## Installation

Create a virtual environment using pipenv:

```bash
pipenv shell
```
Install the following dependencies that will be needed:

```bash
pipenv install -r requirements.txt
```

Create a database instance on [ElephantSQL](https://www.elephantsql.com/), and copy/paste the URL of the instace into the .env folder of the project:

```bash
DATABASE_URL=[YOUR_URL]
```
Setup the database with the project by entering a python shell in the terminal, and then running the following commands:

```bash
>>> from application import db
>>> from application.models import FootballPlayer
>>> db.create_all()
```

## Usage

Run the project by running the dev script. Enter the following in the terminal:

```bash
pipenv run dev
```
### Backend
Using a REST API client extension such as [Thunder Client](https://www.thunderclient.com/), you can perform the following crud operations using the specified paths in the routes.py file:

- Add a footballer using a POST request
- Get a footballers information using a GET request
- Update a footballers information using a PATCH request
- Delete a footballer using a DELETE request

The changes you make using the API routes will reflect on your database instance on ElephantSQL.

### Frontend
A frontend has been implemented using templates that allows you to view all the current players in the database, and provides you with a form to add new players.
