<h1>0x00. AirBnB clone - The console</h1>

<p>This is the first part of the group project in which we where tasked to develop and deploy a simple copy of the AirBnB website. Only  implementing  some of the major features to cover all fundamental concepts of the higher level programming track.</p>
<p>In this first phase, the objective is to create the model files and the console - to emulate the frontend which we will develop in subsequent phases.</p>

<h2>Concepts to learn</h2>
<ul>
<li>Unittest</li>
<li>Python packages concept page</li>
<li>Serialization/Deserialization</li>
<li>*args, **kwargs</li>
<li>datetimeConcepts to learn</li>
<li>More coming soon!</li>
</ul>

<h2>The console</h2>
<h3>Steps:</h3>
<ul>
<li>create your data model
<li>manage (create, update, destroy, etc) objects via a console / command interpreter
<li>store and persist objects to a file (JSON file)
</ul>
<p>The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.<br>
<p>This abstraction will also allow you to change the type of storage easily without updating all of your codebase.<br>
<p>The console will be a tool to validate this storage engine<br>

<h2>What’s a command interpreter?</h2>
<p>The command interpreter is like the command Shell. It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…
<li>Do operations on objects (count, compute stats, etc…)
<li>Update attributes of an object
<li>Destroy an object
</ul>


<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:</p>

<h3>General</h3>
<ul><li>How to create a Python package
<li>How to create a command interpreter in Python using the cmd module
<li>What is Unit testing and how to implement it in a large project
<li>How to serialize and deserialize a Class
<li>How to write and read a JSON file
<li>How to manage datetime
<li>What is an UUID
<li>What is *args and how to use it
<li>What is **kwargs and how to use it
<li>How to handle named arguments in a function</li></ul>

## Execution

  
Your shell should work like this in interactive mode:

  
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```


## Usage Examples

**Launching the console**
```
$ ./console.py
(hbnb) 
```
**Creating a new object**
```
(hbnb) create
** class name missing **
(hbnb) create User
7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
```
**Show an object**
```
(hbnb) show User
** instance id missing **
(hbnb) show User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
[User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433468), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433)}
```
**Update an object**
```
(hbnb) all
[[BaseModel] (27f7849d-1bb9-4cce-9e1e-3d933b2e882d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215829), 'id': '27f7849d-1bb9-4cce-9e1e-3d933b2e882d', 'created_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215822), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (fc9c4248-2f98-4603-a716-27806a356b78) {'updated_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920273), 'id': 'fc9c4248-2f98-4603-a716-27806a356b78', 'created_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920267), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (27dd53e5-e308-4bed-ac3d-eaa2ab4e941d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796849), 'id': '27dd53e5-e308-4bed-ac3d-eaa2ab4e941d', 'created_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796818)}, [User] (d6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114823), 'id': 'd6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114813), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}, [User] (8ce747cb-ce8e-498f-a493-ce415b8a6e6c) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115617), 'id': '8ce747cb-ce8e-498f-a493-ce415b8a6e6c', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115610), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}, [User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433468), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433)}]
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
** attribute name missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61 Age "42"
(hbnb) all
[[BaseModel] (27f7849d-1bb9-4cce-9e1e-3d933b2e882d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215829), 'id': '27f7849d-1bb9-4cce-9e1e-3d933b2e882d', 'created_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215822), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (fc9c4248-2f98-4603-a716-27806a356b78) {'updated_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920273), 'id': 'fc9c4248-2f98-4603-a716-27806a356b78', 'created_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920267), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (27dd53e5-e308-4bed-ac3d-eaa2ab4e941d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796849), 'id': '27dd53e5-e308-4bed-ac3d-eaa2ab4e941d', 'created_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796818)}, [User] (d6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114823), 'id': 'd6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114813), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}, [User] (8ce747cb-ce8e-498f-a493-ce415b8a6e6c) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115617), 'id': '8ce747cb-ce8e-498f-a493-ce415b8a6e6c', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115610), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}, [User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 5, 57, 527661), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433), 'Age': '42'}]
```
**Destroy an object**
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
(hbnb)
```
