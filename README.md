# graphCoV

A web application to represent COVID 19 patient data as a graph.

## Objectives

* To map the spread of the disease.
* To identify clusters of disease spread.

## To do
* Add user authentication
* Show "Person added successfully message" after new person is added.
* Add update person details functionality.
* When link is added, check if nodes exist.
* Add different colors for nodes based on status.



## Dev environment setup (Ubuntu 20.04 LTS)

* Clone the repository.
* Install Anaconda.
* [Create a virtual environment using conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* Activate the virtual environment.
* Install Django, NetworkX and matplotlib:
```
pip3 install django
pip3 install networkx
pip3 install matplotlib
```
* [Install MySQL.](https://linuxconfig.org/install-mysql-on-ubuntu-20-04-lts-linux) (Don't create a new user.) Set password as 'passforMySQL123#'.
* Start MySQL (Run this each time you restart your computer.):
```
sudo service mysql start
```
* Create a database in mysql called 'graphCoV'.
* Run the following commands:
```
sudo apt-get install libmysqlclient-dev
pip3 install mysqlclient
```
* To test your installation, navigate to the folder with 'manage.py' and run:
```
python3 manage.py runserver
```
* Open 'localhost:8000' in a browser window.
* If it works, stop the server and create a superuser:
```
python3 manage.py createsuperuser
```

