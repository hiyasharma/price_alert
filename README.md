# price_alert

**Django Rest Framework Application**

1.**Overview**

This is a Django Rest Framework application that allows users to create, delete, and fetch alerts for cryptocurrency prices. When the price of a specified cryptocurrency meets the alert criteria set by the user, an email notification is sent.

2.**Endpoints**

POST /alerts/create/: Create a new alert.
DELETE /alerts/delete/: Delete an existing alert.
GET /alerts/list/: List all alerts created by the user.

3.**Prerequisites**

Python 3.8+
Django 3.2+
PostgreSQL 12+
Redis (for caching)
RabbitMQ (for message brokering)
Docker (for containerization)

4.**Setup**

Clone the Repository
git clone <repository_url>
cd <repository_directory>
Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

5.**Configure PostgreSQL**

Install PostgreSQL.
Create a database and user.
Update the DATABASES setting in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

6.**Run Migrations**

python manage.py makemigrations
python manage.py migrate

7.**Start the Development Server**

python manage.py runserver


8.**Using the Endpoints**

9.**Create an Alert**
URL: /alerts/create/
Method: POST

10.**Delete an Alert**
URL: /alerts/delete/<alert_id>/
Method: DELETE

11.**List Alerts**
URL: /alerts/list/
Method: GET

12.**Environment Variables**
Create a .env file in the project root and add the following environment variables:


13.**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

14.**Contact**
For any queries or issues, please open an issue in the repository or contact the project maintainers.
