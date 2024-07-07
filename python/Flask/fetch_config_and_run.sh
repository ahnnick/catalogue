#!/bin/bash
source ../../../secrets/catalogue/config.env

# Export the variables so that they are available to subprocesses
export GOOGLE_BOOKS_API_KEY
export SECRET_KEY
export SQLALCHEMY_DATABASE_URI
export SQLALCHEMY_TRACK_MODIFICATIONS


# Debugging: Print environment variables to verify they are set
# echo "GOOGLE_BOOKS_API_KEY: $GOOGLE_BOOKS_API_KEY"
# echo "SECRET_KEY: $SECRET_KEY"
# echo "SQLALCHEMY_DATABASE_URI: $SQLALCHEMY_DATABASE_URI"
# echo "SQLALCHEMY_TRACK_MODIFICATIONS: $SQLALCHEMY_TRACK_MODIFICATIONS"

# Run gunicorn
gunicorn -b 127.0.0.1:5000 main:app
