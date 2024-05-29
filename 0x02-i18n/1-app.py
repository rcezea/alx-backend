#!/usr/bin/env python3
""" Basic Flask Application"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def get_index():
    """The home/index page.
    """
    return render_template('1-index.html')
