# Poject 5-Item Catalog App
This is a project for the Udacity full stack nano degree course.

## APP Info
This project is a web application built using the Flask framework which accesses a SQL database. This app users OAuth2 for authentication and authorization. Currently OAuth2 is implemented for Google Accounts.

The Flask application uses HTML files found in the tempaltes folder for the front-end of the application. Styles and javaScript are stored in the static directory.

## How to run this and use this application

## Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Installation Instructions
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Place the catalog file inside vagrant directory
3. Type inside vagrant directory in the terminal (`vagrant up`)
4. Then type (`vagrant ssh`)
5. Type `cd/vagrant` 
6. Type `python /catalog/catalogdb_setup.py` to setup the database
7. Type `python /catalog/catalogdb_data.py`
8. Now type `python /catalog/application.py` to launch the application
9. Finally open the link http://localhost:5000 to view the application
