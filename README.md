# AirBnB Clone - The Console

## Description
This project is the first step towards building a full web application: an AirBnB clone. It consists of a command interpreter (console) to manage the application's objects, and a base implementation of classes and a file storage system (JSON).

## Command Interpreter
The command interpreter is a custom shell used for data management. It allows you to create, retrieve, update, and destroy objects (like Users, Places, States, Cities, etc.) from the command line.

### How to start it
Run the `console.py` script from the root of the repository:
```bash
$ ./console.py
```

### How to use it
The console can be used in an interactive mode or a non-interactive mode. In interactive mode, a prompt `(hbnb)` is displayed, waiting for your commands.

Commands available include:
* `help` - Show all available commands or get help on a specific command.
* `quit` or `EOF` - Exit the console.

### Examples

**Interactive mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```

**Non-interactive mode:**
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```