# config.py
import os

class Config:

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'data', 'site.db')    
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ.get('SECRET_KEY')
	GOOGLE_BOOKS_API_KEY = os.environ.get('GOOGLE_BOOKS_API_KEY') 
