from flask import Flask     # Server & Routes
from flask import request   # Parsing HTTP requests
from flask import jsonify   # Converting Python dictionaries into JSON

from peewee import *        # Python Classes to SQL Tables
from playhouse.shortcuts import model_to_dict   # Convert Peewee Model to Dictionary

# Create our database object for Python
# Assumes we have a database called 'people' and a user named 'postgres'
db = PostgresqlDatabase('people', user='postgres', password='', host='localhost', port=5432)

# Base model that all models will extend from that establishes relationship to database
class BaseModel(Model):
    class Meta:
        database = db

# Our Person model, has two fields: first and last name, that are type "CharField"
class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()

class Pet(BaseModel):
    name = CharField()

db.connect()    # Connect to the database 
db.drop_tables([Person, Pet])    # Drop the Person table (in case it already exists)
db.create_tables([Person, Pet])  # Create the Person table

# Create and save two instances of our Person model
tyler = Person(first_name='Tyler', last_name='Lane')
nora = Person(first_name='Nora', last_name='Tulchina')
tyler.save()
nora.save()

cat1 = Pet(name='Flopsy')
cat2 = Pet(name='Mittens')
cat1.save()
cat2.save()


# Create our Flask App
app = Flask(__name__)


# Define a '/person' endpoint that accepts GET requests
@app.route('/person', methods=['GET'])
@app.route('/person/<id>', methods=['GET'])
def person(id=None):
    if id:
        person = Person.get(Person.id == id)
        person = model_to_dict(person)
        return jsonify(person)
    else:
        people = []
        # Iterate over a query that gets every Person
        for person in Person.select():
            # Convert each person from Python object to Dictionary
            people.append(model_to_dict(person))
        # Convert list of dictionaries into JSON and return to server
        return jsonify(people)


@app.route('/pet', methods=['GET'])
def pet():
    pets = []
    for pet in Pet.select():
        pets.append(model_to_dict(pet))
    return jsonify(pets)


# Start server, listen on port 9000 and re-start server on file change
app.run(port=9000, debug=True)