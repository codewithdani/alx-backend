#!/usr/bin/env python3
"""
Flask app with a single / route
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('0-index.html',
                           title="Welcome to Holberton",
                           header="Hello world")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
