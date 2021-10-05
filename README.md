# PyLadies Website
The website for PyLadies Ghana.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)
* [License](#license)
* [Contributing](#contributing)


## General info
The website for PyLadies Ghana. 


## Technologies
* Python 3.7
* Django 2.2
* HTML5
* CSS3 
* Bootstrap4 
* Font awesome

### Setup
## Installation on Linux and Mac OS

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  sudo apt-get install python-virtualenv
  
  virtualenv --python=python3.6.5 myvenv
  
  source myvenv/bin/activate

  (myvenv) $ pip install -r requirements.txt

  (myvenv) $ python manage.py makemigrations

  (myvenv) $ python manage.py migrate

  (myvenv) $ python manage.py runserver
  ```
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.


## Installation on Windows

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  1. Create main project folder with name of your choice (eg.PyLadies) 
  
  2. Clone (git clone url) the project into that folder.
   
  3. Open the command prompt and navigate the project folder (PyLadies)
  
  4. virtualenv pyladies_venv   # Create a virtual environment for the project with it's own packages.
  
  5. pyladies_venv\Scripts\activate    # Move into the virtual environment folder and activate the environment.
  
  6. cd PyLadies-Website   # Move into project (PyLadies-Website) folder.
  
  7. pip install -r requirements.txt  # install the requirements.

  8. python manage.py migrate   # Migrate the data into the database.

  9. python manage.py runserver   # Run the server.
  
  NOTE: You can use any text editor or IDE of your choice. 
  ```
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.


## Status
Project is: _in progress_

## Contact
Created by [PyLadies](mailto:ghana@pyladies.com) - feel free to contact us!

## License
>You can check out the full license [here](https://github.com/pyladiesghana/PyLadies-Website/blob/master/LICENSE)

This project is licensed under the terms of the **MIT** license.

## Contributing

1. Fork it (<https://github.com/pyladiesghana/PyLadies-Website.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
