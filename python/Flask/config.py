# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_BOOKS_API_KEY = os.environ.get('GOOGLE_BOOKS_API_KEY') 