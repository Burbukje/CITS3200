# Food Atlas Project
TODO

## Requirements
- python3
- Django
- venv
- sqlite3

## Getting Started
Create virtual environment: 

For Unix/macOS

1. Create the virtual environment. (Should be pre-installed with python distros).
```python
# python3
$ python3 -m venv venv
```

2. Activate the environment.
```python
# activate environment for unix machines
$ source venv/bin/activate
```

3. Install requirements.
```python
pip install -r requirements.txt

# if pip doesnt work try
pip3 install -r requirements.txt
```

4. Deactivate environment
```python
$ deactivate
```

For Windows 
1. Create the environment
```python
$ py -m venv venv
```

2. Activate the environment. You may have to enable scripts to be run.

For more information.

https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system

```python
# activate environment for windows
$ venv\Scripts\activate
```

3. Install requirements using the "requirements.txt".
```python
$ pip install -r requirements.txt
```

4. Deactivate environment
```python
$ deactivate
```

#

## Running the app

Go to the root directory where Dockerfile and docker-compose.yml are
First run  `docker-compose build`
After that, run  `docker-compose up`
Open the app through http://0.0.0.0:8000/ 

### Important
Everytime you make a change to the code, remember to run `docker-compose build` first and then run `docker-compose up`

## Migrating the DataBase

Ensure you are in the directory with the manage.py file

1. Update the database schema
```python
$ python manage.py makemigrations
```
2. Create the database
```python
$ python manage.py migrate
```

The database should be up and running, you can view the database in the Admin page

## Accessing the Admin page

TODO: Register models in admin.py so you can see the database.

To access the admin page simply add `/admin` at the end of the address
```
username: admin
password atlantides
```

#

## Running unit tests
To run unit tests simply run the command

```python
$ python3 manage.py test
```

## Deployment
TBC

## Running Tests
TBC

## Built With
Windows, Linux, MacOS

VScode

Python3 3.6+

Django

Github

## Contributing
Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
0.00 - Sprint 1 

## Authors
* Tom Nguyen
* Bea Shakjiri
* Taj Bishop
* Wei Hong Tan
* Rodney Cham

## License
TBC

## Acknowledgments

