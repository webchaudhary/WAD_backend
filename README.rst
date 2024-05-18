Instructions
=============

* Create a Python 3 virtual environment in the webapp directory

``virtualenv -p /usr/bin/python3 venv``

`python3 -m venv venv`
`. venv/bin/activate`


* Activate the virtual environment

``source venv/bin/activate``

* Install dependencies with `pip`

``pip install -r requirements.txt``
``pip3 freeze > requirements.txt``

* Set connection to the database and create its structure

  ```bash
  cd wagen

  # add user, password and grass settings in wagen/settings.py
  python manage.py makemigrations webapp
  python manage.py migrate

  # create a new user to access the features of web app
  python manage.py createsuperuser --username admin

  # to see the help
  python manage.py help
  ```



TESTING
^^^^^^^

To attach a screen : 
`screen -r 392898.django_server`
`screen -r 393313.celery_worker`
Then control+ C =

Detach a screen
`screen -d 404581.celery_worker`

To delete a screen 
`screen -S 356415.celery_worker -X quit`

Start a new screen
`screen -S django_server`
`screen -S celery_worker`



* Start celery worker to use asynchronous requests

  `celery -A wagen worker -l INFO`

* At this point you could run the app

  `python3 manage.py runserver`
  .. run this access on other device too: 
`python manage.py runserver 0.0.0.0:8000`
  .. After running this you can access the dashboard on otherdevice too at "http://10.37.129.2:8000/"


* Open web browser at http://127.0.0.1:8000/


