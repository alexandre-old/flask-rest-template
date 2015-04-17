import datetime


# database connection data
DB_CONNECTION = {
    "MONGODB_DB": "",
    "MONGODB_USERNAME": "",
    "MONGODB_PASSWORD": "",
    "MONGODB_HOST": "",
    "MONGODB_PORT": 27017
}

# database uri
DATABASE_URI = ''

# flask vars
FLASK_VARS = {
    'SECRET_KEY': '',
}

# flask-jwt vars
FLASK_JWT_VARS = {
    'JWT_AUTH_URL_RULE': '',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1)
}

# another third party libs...
