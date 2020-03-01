# AirBnB Console

A command interpreter is the part of a system that understands and executes commands that are entered interactively by a human being or from a program.

This is the step 1/4 towards building a full web application: an AirBnB clone. This first step is used among all other following projects: HTML/CSS templating, database storage, API, front-end integration


## Description

This command interpreter is limited to a specific use-case. We want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


## How to start it

After cloning the repository, you have to give permissions if it is necessary and then run the `console.py` file:

```python

./console.py
```

The result should be something like this:

```python
(hbnb) 
```

where `(hbnb)` is the prompt of the line interpreter


## Types of classes to manipulate

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review


## Commands enabled

- __create__: Creates a new instance and saves it (to a JSON file).
- __show__: Prints the string representation of an instance based on the class name and id.
- __destroy__: Deletes an instance based on the class name and id (save the change into the JSON file).
- __all__: Prints all string representation of all instances based or not on the class name.
- __update__: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
- __quit__: Exit the program

## Examples

```python
(hbnb) create USer
** class doesn't exist **
(hbnb) create User
0fc24e4f-7aa6-418e-bb11-83fc92122755
(hbnb) show User
** instance id missing **
(hbnb) show User 0fc24e4f-7aa6-418e-bb11-83fc92122755
[User] (0fc24e4f-7aa6-418e-bb11-83fc92122755) {'id': '0fc24e4f-7aa6-418e-bb11-83fc92122755', 'created_at': datetime.datetime(2020, 2, 19, 15, 37, 13, 327), 'updated_at': datetime.datetime(2020, 2, 19, 15, 37, 31, 913062)}
(hbnb) all User
["[User] (22a3fc03-dc81-4117-b363-f4775bff55db) {'id': '22a3fc03-dc81-4117-b363-f4775bff55db', 'created_at': datetime.datetime(2020, 2, 19, 13, 19, 20, 865945), 'updated_at': datetime.datetime(2020, 2, 19, 13, 19, 20, 865948), 'first_name': 'Kev', 'last_name': 'Yo', 'email': '1234@yahoo.com'}", "[User] (123455) {'id': '123455', 'created_at': datetime.datetime(2020, 2, 19, 13, 19, 20, 866157), 'updated_at': datetime.datetime(2020, 2, 19, 13, 19, 20, 866158), 'name': 'Kevin'}", "[User] (123455) {'id': '123455', 'created_at': datetime.datetime(2020, 2, 19, 13, 19, 20, 866157), 'updated_at': datetime.datetime(2020, 2, 19, 13, 19, 20, 866158), 'name': 'Kevin'}", "[User] (0fc24e4f-7aa6-418e-bb11-83fc92122755) {'id': '0fc24e4f-7aa6-418e-bb11-83fc92122755', 'created_at': datetime.datetime(2020, 2, 19, 15, 37, 13, 327), 'updated_at': datetime.datetime(2020, 2, 19, 15, 37, 31, 913062)}"]
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit

Process finished with exit code 0
```

## Languaje

python 3.7.5


## Authors

- Camilo Isaza [Twitter](https://twitter.com/andresmelek/) 
- Simón Parra [Twitter](https://twitter.com/Simonster04/)

ENJOY IT PAPU! :bowtie:  :bowtie:  :bowtie:
