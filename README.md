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

<h2>Copyright - Plagiarism</h2>
<ul><li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
<li>You are not allowed to publish any content of this project.
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li></ul>

<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul><li>Allowed editors: vi, vim, emacs
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
<li>All your files should end with a new line
<li>The first line of all your files should be exactly #!/usr/bin/python3
<li>A README.md file, at the root of the folder of the project, is mandatory
<li>Your code should use the pycodestyle (version 2.8.*)
<li>All your files must be executable
<li>The length of your files will be tested using wc
<li>All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
<li>All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
<li>All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li></ul>

<h3Python Unit Tests</h3>
<ul><li>Allowed editors: vi, vim, emacs
<li>All your files should end with a new line
<li>All your test files should be inside a folder tests
<li>You have to use the unittest module
<li>All your test files should be python files (extension: .py)
<li>All your test files and folders should start by test_
<li>Your file organization in the tests folder should be the same as your project
<li>e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
<li>e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
<li>All your tests should be executed by using this command: python3 -m unittest discover tests
<li>You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
<li>All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
<li>All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
<li>All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
<li>We strongly encourage you to work together on test cases, so that you don’t miss any edge case</ul>
