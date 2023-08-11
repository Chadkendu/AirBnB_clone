# 0x00. AirBnB clone - The console

## What is a CLI (Command Line Interpreter)

A `CLI` is a text-based User-Interface that runs commands and computer programes. It acts just like the shell.

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3 (version 3.8.5)`
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using wc
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle (version 2.8.*)`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- You have to use the `unittest` module
- All your test files should be inside a folder `./tests`
- All your test files should be python files `(extension: .py)`
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
- > e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- > e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py



## Classes Needed in this Project

|   Classes -->  | BaseModel | User | State | City | Amenity | Place | Review | FileStorage |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **Public Instance Attributes** | `id`<br>`created_at`<br>`updated_at` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | --- |
| **Public Instance Methods** |`save()`<br>`to_dict()` | --- | --- | --- | --- | --- | --- | `all()`<br>`new()`<br>`save()`<br>`reload()` |
| **Public Class Attributes** | --- | `email`<br>`first_name`<br>`last_name`<br>`password`| `name` | `name`<br>`state_id` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | --- |
| **Private Class Attributes** | --- | --- | --- | --- | --- | --- | --- | `__file_path`<br>`__objects` |

## How the program is executed

### In interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### In non-interactive mode: (just like the simple shell project in C language)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

CONTRIBUTORS

A. JOSHUA AJAYI
B. NOHA FATHY
