# Django Exercise

A simple project to register a user and save geo details from given address

### Instructions to run

* Pull the code from the repository
* Install system dependencies (RabbitMQ server for celery broker)
  
  ```
  $ sudo apt-get install rabbitmq-server
  $ sudo service rabbitmq-server start
  ```
  Or for Mac
  ```
  $ brew install rabbitmq
  $ /usr/local/sbin/rabbitmq-server
  ```
* Create python virtualenv and activate it
  ```
  $ virtualenv exerciseenv  
  $ source exerciseenv/bin/activate
  ```
* Install dependencies. `cd` to project directory and run:-
  ```
  $ pip install -r requirements.txt
  ```
* Set OS environment variable `sudo vim ~/.bash_profile` and add the line
  ```
  export GOOGLE_API_KEY="<Google API key>"
  ```
  This API key is for accessing the [Google Maps Geocode](https://developers.google.com/maps/documentation/geocoding/intro) API
* Run celery worker in other terminal window/tab
  ```
  celery -A exercise worker -l info
  ```
* Run migrations
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
* Run the django development server
  ```
  $ python manage.py runserver
  ```
* Test the User registration API from any HTTP Client.

  Make a `POST` request on `http://127.0.0.1:8000/users/registration/`
  
  PAYLOAD:
  ```javascript
  {
    "name" : "Test Exercise",
    "email" : "test.exercise@gmail.com",
    "password" : "test",
    "address" : "Ahmedabad, India"
  }
  ```
  
  RESPONSE:
  ```javascript
  {
  "message": "User registered successfully",
  "user_id": 1
  }
  ```
  
  This API then triggers background task `registration.tasks.save_geo_details` for saving latitude & longitude for the user. You can view the data in the database `exercise/db.sqlite3` in table `registration_user`
  

* To use Bing Maps API instead of Google Maps API, just initiate the `BingMapsGeoLocation` class in the `registration/tasks.py`
   ```python
   from geolocation import BingMapsGeoLocation
   geolocation_obj = BingMapsGeoLocation(os.environ.get('BING_API_KEY'))
    ```