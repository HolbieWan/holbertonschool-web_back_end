# NoSQL

## What NoSQL means
NoSQL refers to “non-relational” databases that store and retrieve data in formats other than traditional tabular rows and columns.

+ Instead of using tables with rows and columns, a NoSQL database might store data as JSON objects.
+ **Real-World Example:** A NoSQL database like MongoDB stores user profiles as flexible JSON-like documents.

## What is difference between SQL and NoSQL
SQL databases use structured, table-based schemas, while NoSQL databases are more flexible and can handle unstructured or semi-structured data.
+ SQL stores data in structured tables, NoSQL stores data as key-value pairs or documents.
+ **Real-World Example:** An e-commerce site uses MySQL for order tracking (structured data) and MongoDB for product reviews (unstructured data).

## What is ACID
ACID stands for Atomicity, Consistency, Isolation, and Durability, ensuring reliable database transactions in SQL systems.
+ When transferring money between two accounts, all steps of the transaction succeed or none do (Atomicity).
+ **Real-World Example:** Booking a flight through an airline’s system ensures no double-booking due to ACID compliance.

## What is a document storage
Document storage is a NoSQL data model that stores data as documents, often in formats like JSON or BSON.
+ **Theoretical Example:** A customer profile is stored as a single JSON document with fields like name, age, and preferences.
+ **Real-World Example:** MongoDB stores a blog post as a document with the post content, author, and tags.

## What are NoSQL types
NoSQL databases are categorized into types like document, key-value, column-family, and graph databases.
+ **Theoretical Example:** A key-value store saves data as key: value pairs; a graph database uses nodes and edges.
+ **Real-World Example:** Redis is a key-value database, while Neo4j is a graph database.

## What are benefits of a NoSQL database
NoSQL databases provide flexibility, scalability, and high performance for modern, large-scale applications.
+ **Theoretical Example:** NoSQL adapts easily to changing data formats or schema designs.
+ **Real-World Example:** Netflix uses NoSQL databases to handle massive, dynamic user data at scale.

## How to query information from a NoSQL database
NoSQL databases use non-SQL query languages, like MongoDB’s query language or Cassandra Query Language (CQL).
+ **Theoretical Example:** Query MongoDB with {name: "John"} to find all documents where name equals “John.”
+ **Real-World Example:** Find all users in a MongoDB collection whose age is greater than 30 with:

```javascript
db.users.find({ age: { $gt: 30 } });
```

## How to insert/update/delete information from a NoSQL database
NoSQL databases provide specific methods or APIs for inserting, updating, or deleting data.

**Theoretical Example:**
+ Insert: db.collection.insertOne({name: "John", age: 30})
+ Update: db.collection.updateOne({name: "John"}, {$set: {age: 31}})
+ Delete: db.collection.deleteOne({name: "John"})

**Real-World Example:**
```javascript
db.products.insertOne({ name: "Laptop", price: 1000 });
db.products.updateOne({ name: "Laptop" }, { $set: { price: 900 } });
db.products.deleteOne({ name: "Laptop" });
```

## How to use MongoDB
MongoDB is a NoSQL database that stores data as JSON-like documents. It can be used locally or via cloud services like MongoDB Atlas.

#### 1-Install MongoDB
<a https://www.mongodb.com/docs/manual/tutorial/install-mongodb-enterprise-on-os-x/>

#### 2-Start the MongoDB server
```bash
mongod
```

 #### 3-Use the mongo shell to interact with databases:

**Running the mongo Shell**
```shell
mongo
```

**Establishing a Connection**
```shell
> db
test
>
```

```shell
> use rptutorials
switched to db rptutorials
```
```shell

> show dbs
admin          0.000GB
config         0.000GB
local          0.000GB
>
```

**Creating Collections and Documents**

```shell
> use rptutorials
switched to db rptutorials
> db
rptutorials
> db.tutorial
rptutorials.tutorial
```
**Exemple of document:**
```shell
{
    "title": "Reading and Writing CSV Files in Python",
    "author": "Jon",
    "contributors": [
        "Aldren",
        "Geir Arne",
        "Joanna",
        "Jason"
    ],
    "url": "https://realpython.com/python-csv/"
}
```

**Working With Collections and Documents**

To insert a document into a database using the mongo shell, you first need to choose a collection and then call **.insertOne()** on the collection with your document as an argument:

```shell
> use rptutorials
switched to db rptutorials

> db.tutorial.insertOne({
...     "title": "Reading and Writing CSV Files in Python",
...     "author": "Jon",
...     "contributors": [
...         "Aldren",
...         "Geir Arne",
...         "Joanna",
...         "Jason"
...     ],
...     "url": "https://realpython.com/python-csv/"
... })
{
    "acknowledged" : true,
    "insertedId" : ObjectId("600747355e6ea8d224f754ba")
}
```

**Other example:**

```javascript
db.inventory.insertOne({ item: "notebook", qty: 50 });
```

**using .insertMany():**
```shell
> tutorial1 = {
...     "title": "How to Iterate Through a Dictionary in Python",
...     "author": "Leodanis",
...     "contributors": [
...         "Aldren",
...         "Jim",
...         "Joanna"
...     ],
...     "url": "https://realpython.com/iterate-through-dictionary-python/"
... }

> tutorial2 = {
...      "title": "Python 3's f-Strings: An Improved String Formatting Syntax",
...      "author": "Joanna",
...      "contributors": [
...          "Adriana",
...          "David",
...          "Dan",
...          "Jim",
...          "Pavel"
...      ],
...      "url": "https://realpython.com/python-f-strings/"
... }

> db.tutorial.insertMany([tutorial1, tutorial2])
{
    "acknowledged" : true,
    "insertedIds" : [
        ObjectId("60074ff05e6ea8d224f754bb"),
        ObjectId("60074ff05e6ea8d224f754bc")
    ]
}
```

**use .find() to retrieve the documents in a collection:**
```shell
> db.tutorial.find()
{ "_id" : ObjectId("600747355e6ea8d224f754ba"),
"title" : "Reading and Writing CSV Files in Python",
"author" : "Jon",
"contributors" : [ "Aldren", "Geir Arne", "Joanna", "Jason" ],
"url" : "https://realpython.com/python-csv/" }
    ...

> db.tutorial.find({author: "Joanna"})
{ "_id" : ObjectId("60074ff05e6ea8d224f754bc"),
"title" : "Python 3's f-Strings: An Improved String Formatting Syntax (Guide)",
"author" : "Joanna",
"contributors" : [ "Adriana", "David", "Dan", "Jim", "Pavel" ],
"url" : "https://realpython.com/python-f-strings/" }
```
---

## Using MongoDB With Python and PyMongo

### Installing PyMongo

```shell
$ pip install pymongo==3.11.2
```

```python
>>> import pymongo
```

### Establishing a Connection

```python
>>> from pymongo import MongoClient
>>> client = MongoClient()
>>> client
MongoClient(host=['localhost:27017'], ..., connect=True)
```

For custom host and port:
```python
>>> client = MongoClient(host="localhost", port=27017)
```

or use  MongoDB URI format:
```python
>>> client = MongoClient("mongodb://localhost:27017")
```

### Working With Databases, Collections, and Documents

```python
>>> db = client.rptutorials
>>> db
Database(MongoClient(host=['localhost:27017'], ..., connect=True), 'rptutorials')
```

You can also use dictionary-style access if the name of the database isn’t a valid Python identifier:
```python
>>> db = client["rptutorials"]
```

In Python, you use dictionaries to create documents:
```python
>>> tutorial1 = {
...     "title": "Working With JSON Data in Python",
...     "author": "Lucas",
...     "contributors": [
...         "Aldren",
...         "Dan",
...         "Joanna"
...     ],
...     "url": "https://realpython.com/python-json/"
... }
```

Once you’ve created the document as a dictionary, you need to specify which collection you want to use. To do that, you can use the dot notation on the database object:
```python
>>> tutorial = db.tutorial
>>> tutorial
Collection(Database(..., connect=True), 'rptutorials'), 'tutorial')
```

In this case, tutorial is an instance of Collection and represents a physical collection of documents in your database. You can insert documents into tutorial by calling .insert_one() on it with a document as an argument:
```python
>>> result = tutorial.insert_one(tutorial1)
>>> result
<pymongo.results.InsertOneResult object at 0x7fa854f506c0>

>>> print(f"One tutorial: {result.inserted_id}")
One tutorial: 60084b7d87eb0fbf73dbf71d
```

Here, .insert_one() takes tutorial1, inserts it into the tutorial collection and returns an InsertOneResult object. This object provides feedback on the inserted document. Note that since MongoDB generates the ObjectId dynamically, your output won’t match the ObjectId shown above.

If you have many documents to add to the database, then you can use .insert_many() to insert them in one go:
```python
>>> tutorial2 = {
...     "title": "Python's Requests Library (Guide)",
...     "author": "Alex",
...     "contributors": [
...         "Aldren",
...         "Brad",
...         "Joanna"
...     ],
...     "url": "https://realpython.com/python-requests/"
... }

>>> tutorial3 = {
...     "title": "Object-Oriented Programming (OOP) in Python 3",
...     "author": "David",
...     "contributors": [
...         "Aldren",
...         "Joanna",
...         "Jacob"
...     ],
...     "url": "https://realpython.com/python3-object-oriented-programming/"
... }

>>> new_result = tutorial.insert_many([tutorial2, tutorial3])

>>> print(f"Multiple tutorials: {new_result.inserted_ids}")
Multiple tutorials: [
   ObjectId('6008511c87eb0fbf73dbf71e'),
   ObjectId('6008511c87eb0fbf73dbf71f')
]
```

This is faster and more straightforward than calling .insert_one() multiple times. The call to .insert_many() takes an iterable of documents and inserts them into the tutorial collection in your rptutorials database. The method returns an instance of InsertManyResult, which provides information on the inserted documents.

To retrieve documents from a collection, you can use .find(). Without arguments, .find() returns a Cursor object that yields the documents in the collection on demand:
```python
>>> import pprint

>>> for doc in tutorial.find():
...     pprint.pprint(doc)
...
{'_id': ObjectId('600747355e6ea8d224f754ba'),
 'author': 'Jon',
 'contributors': ['Aldren', 'Geir Arne', 'Joanna', 'Jason'],
 'title': 'Reading and Writing CSV Files in Python',
 'url': 'https://realpython.com/python-csv/'}
    ...
{'_id': ObjectId('6008511c87eb0fbf73dbf71f'),
 'author': 'David',
 'contributors': ['Aldren', 'Joanna', 'Jacob'],
 'title': 'Object-Oriented Programming (OOP) in Python 3',
 'url': 'https://realpython.com/python3-object-oriented-programming/'}
```

Here, you run a loop on the object that .find() returns and print successive results, using pprint.pprint() to provide a user-friendly output format.

You can also use .find_one() to retrieve a single document. In this case, you can use a dictionary that contains fields to match. For example, if you want to retrieve the first tutorial by Jon, then you can do something like this:


```python
>>> import pprint

>>> jon_tutorial = tutorial.find_one({"author": "Jon"})

>>> pprint.pprint(jon_tutorial)
{'_id': ObjectId('600747355e6ea8d224f754ba'),
 'author': 'Jon',
 'contributors': ['Aldren', 'Geir Arne', 'Joanna', 'Jason'],
 'title': 'Reading and Writing CSV Files in Python',
 'url': 'https://realpython.com/python-csv/'}
```

### Closing Connections

You can close the connection by calling .close() on the MongoClient instance:
```python
>>> client.close()
```

Another situation is when you have an application that occasionally uses a MongoDB database. In this case, you might want to open the connection when needed and close it immediately after use for freeing the acquired resources. A consistent approach to this problem would be to use the with statement. Yes, MongoClient implements the context manager protocol:
```python
>>> import pprint
>>> from pymongo import MongoClient

>>> with MongoClient() as client:
...     db = client.rptutorials
...     for doc in db.tutorial.find():
...         pprint.pprint(doc)
...
{'_id': ObjectId('600747355e6ea8d224f754ba'),
 'author': 'Jon',
 'contributors': ['Aldren', 'Geir Arne', 'Joanna', 'Jason'],
 'title': 'Reading and Writing CSV Files in Python',
 'url': 'https://realpython.com/python-csv/'}
    ...
{'_id': ObjectId('6008511c87eb0fbf73dbf71f'),
 'author': 'David',
 'contributors': ['Aldren', 'Joanna', 'Jacob'],
 'title': 'Object-Oriented Programming (OOP) in Python 3',
 'url': 'https://realpython.com/python3-object-oriented-programming/'}
```


```python

```


```python

```


```python

```


```python

```