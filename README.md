## Holberton HBnB: The BEST AirBnB clone out there!

----------------------------------------

**Authors**
- **Philip Yoo**, \<philip.yoo@holbertonschool.com>, @philipYoo10
- **Jianqin Wang**, \<jianqin.wang@holbertonschool.com>, @jianqinwang94

----------------------------------------

This is a website clone of AirBnB, with the fundamental features implemented.
It has a front-end, a database, an API for front-end to database communication,
and a developer command line interface.

The command line interface allows use of CRUD operations on the data objects in
the database, as well as special operations like counting, computing stats,
etc.


### How to start console

To run the console, type in: ```$ ./console.py```

### How to use console

The HBnB console supports the essential CRUD operations to manipulate data.
This data can be stored in two ways: SQL database and JSON file.


#### Create:

```(hbnb) create <classname> <optionalparam1=value1> <optionalparam2=value2> ...```


#### Read:

```(hbnb) all <optionalclassname>```

```(hbnb) show <classname> <id>```


#### Update:

```(hbnb) update <classname> <id> <param1=value1> <param2=value2> ... <lastparam=lastvalue>```


#### Delete:

```(hbnb) destroy <classname> <id>```



### Alternate Syntax:



#### Read:

```(hbnb) <classname>.all()```

```(hbnb) <classname>.show(<id>)```


#### Update:

```(hbnb) <classname>.update(<id>, {dictionary_of_params})```

```(hbnb) <classnam>.update(<id>, <param1=value1, <param2=value2>, ...)```



*Additionally, you can count the number of objects in a class like so:*

```(hbnb) <classname>.count()```
