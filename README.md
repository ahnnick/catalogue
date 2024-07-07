# How to test

## The Flask app
```
cd book-catalogue/python/Flask
Python3 -m venv venv/testing; source venv/testing/bin/Activate
#ensure you are in the virtual environment, then install dependencies:
Python3 -m pip install -r requirements.txt
./fetch_config_and_run.sh
```
Navigate to http://127.0.0.1:5000/ to visit the site. 

Cleanup: 
```
#interrupt the process, then
deactivate
#...to exit the virtual environment
rm -rf venv/testing
```
