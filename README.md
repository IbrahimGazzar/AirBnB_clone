<h1>0x00. AirBnB clone - The console</h1>

<p>This is the first part of the group project in which we where tasked to develop and deploy a simple copy of the AirBnB website. Only  implementing  some of the major features to cover all fundamental concepts of the higher level programming track.</p>
<p>In this first phase, the objective is to create the model files and the console - to emulate the frontend which we will develop in subsequent phases.</p>

<h2>Concepts to learn</h2>
<ul>
<li>Unittest - and please work all together on tests cases
<li>Python packages concept page
<li>Serialization/Deserialization
<li>*args, **kwargs
<li>datetime
<li>More coming soon!

<h2>The console</h2>
<h3>Steps:</h3>

create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

