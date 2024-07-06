import os
from app import create_app, db


data_dir = os.path.join(os.getcwd(), 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Print current working directory and database path for debugging
print(f"Current working directory: {os.getcwd()}")
print(f"Data directory: {data_dir}")
print(f"Database path: {os.path.join(data_dir, 'site.db')}")

def create_database(app):
    print("Checking for existing database...")
    if not os.path.exists(os.path.join(data_dir, 'site.db')):
        print("Database does not exist. Creating now...")
        with app.app_context():
            try:
                db.create_all()
                print("Database created.")
            except Exception as e:
                print(f"Error creating database: {e}")
    else:
        print("Database already exists.")

app = create_app()

if __name__ == '__main__':
	app = create_app()
	create_database(app)
	app.run(debug=True)
