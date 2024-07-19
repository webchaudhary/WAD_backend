
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
  cd backend

  # add user, password and grass settings in backend/settings.py

  `python manage.py makemigrations webapp``
  `python manage.py migrate``
  `python manage.py collectstatic`


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



* At this point you could run the app
`python manage.py runserver 0.0.0.0:8000`


* Open web browser at http://127.0.0.1:8000/






=================================================================
Restart  uWSGI in development after updates
=================================================================


# To stop uWSGI
`killall uwsgi`

#Restart uWSGI (first activate the venv)
`uwsgi --ini backend_dashboard.ini`



=============
Apache commands
=============


* Enable the virtual host with the following command:**
`sudo a2ensite dashboards-backend.conf`

* To disable site**
(here dashboards-backend.conf is apache conf file for global.waterinag.org website)
`sudo a2dissite dashboards-backend.conf`


* Restart the Apache webserver to apply the changes:
`sudo systemctl reload apache2`
`sudo systemctl restart apache2`

* List all the enabled sites**
`ls -l /etc/apache2/sites-enabled`

* Test the apache configuration:**
`sudo apachectl configtest`


* Install certbot in Ubuntu (enable ssl certificate)
`sudo apt install certbot python3-certbot-apache`

* Set SSL and enable https**
`sudo certbot --apache -d backend.waterinag.org`




=============
Possible errors
=============


# Check the socket file permissions after starting uWSGI:
`tail -f /home/aman/dashboards_backend/backend/log/backend_dashboard.log`
`sudo tail -f /home/aman/dashboards_backend/backend/log/backend_dashboard.log`

# If permission errors occurred
`sudo chown -R www-data:www-data /home/aman/dashboards_backend/backend
sudo chown -R aman:aman /home/aman/dashboards_backend/backend/log/
sudo chmod -R 755 /home/aman/dashboards_backend/backend/log/
`

sudo chown aman:aman /home/aman/dashboards_backend/backend/backend_dashboard.sock



# check uWSGI log
`tail -f /home/aman/dashboards_backend/backend/log/backend_dashboard.log`


# check apache log if errors
`sudo tail -f /var/log/apache2/dashboard_backend_error.log`
`sudo tail -f /var/log/apache2/dashboard_backend_access.log`

# Ensure Apache Configuration Points to Correct Socket

# If issue while crateating uwsgi .sock file then run with sudo
`sudo uwsgi --ini /home/aman/dashboards_backend/backend/backend_dashboard.ini`




