import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

data_dir = os.path.join(os.getcwd(), 'data')
if not os.path.exists(data_dir):
	os.makedirs(data_dir)

def create_app(): 
	catalogue = Flask(__name__)
	
	catalogue.config.from_object('config.Config')

#	catalogue.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(data_dir, 'site.db')
#	catalogue.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# Debug prints to verify environment variables
	print(f"SECRET_KEY: {catalogue.config['SECRET_KEY']}")
	print(f"SQLALCHEMY_DATABASE_URI: {catalogue.config['SQLALCHEMY_DATABASE_URI']}")
	
	db.init_app(catalogue)
	migrate.init_app(catalogue, db)	

	from . import routes
	catalogue.register_blueprint(routes.catalogue)

	return catalogue
