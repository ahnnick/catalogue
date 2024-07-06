# How to test

## Flask
```
cd book-catalogue/python/Flask/venv
Python3 -m venv testing; source testing/bin/Activate
#ensure you are in the virtual environment, then install dependencies:
Python3 -m pip install -r ../requirements.txt
#launch app. todo: replace this with gunicorn
Python3 main.py
```
Navigate to http://127.0.0.1:5000/ to visit the site. 

Cleanup: 
```
#interrupt the process, then
deactivate
#...to exit the virtual environment
rm -rf testing
```
