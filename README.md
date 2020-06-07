# graphCoV

A web application to represent COVID 19 patient data as a graph.

## Objectives

* To map the spread of the disease.
* To identify clusters of disease spread.

## Dev environment setup

* Clone the repository.
* Install Anaconda.
* [Create a virtual environment using conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* Activate the virtual environment.
* Install Django:
```
pip3 install django
```
* [Install mysql.](https://linuxconfig.org/install-mysql-on-ubuntu-20-04-lts-linux) (Don't create a new user.) Set password as 'passforMySQL123#'.
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


