#!bin/sh

export FLASK_ENV=development
export FLASK_APP=app.py

flask run --reload --host 0.0.0.0 --port 5000