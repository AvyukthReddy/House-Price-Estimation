# House-Price-Prediction:

1. Deployed on Heroku (https://house-price-prediction-heroku.herokuapp.com/)
2. Deployed on Render (https://house-price-prediction-04wg.onrender.com/)

## Setup and Run

Follow these steps to set up and run the project:

1. Clone the repository: `git clone "https://github.com/AvyukthReddy/House-Price-Prediction"`
2. Install virtualenv (skip if installed): `pip install virtualenv`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment: `.venv\Scripts\activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Run the application: `python app.py`

# Flask

Flask is a lightweight `WSGI` web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`
and `Jinja` and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

WSGI: https://wsgi.readthedocs.io/
Werkzeug: https://werkzeug.palletsprojects.com/
Jinja: https://jinja.palletsprojects.com/

## Installing

Install and update using `pip`:

code-block:: text

$ pip install -U Flask

pip: https://pip.pypa.io/en/stable/getting-started/

## A Simple Example

code-block:: python

# save this as app.py

from flask import Flask

app = Flask(**name**)

@app.route("/")
    def hello():
        return "Hello, World!"

code-block:: text

$ flask run
      \* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
