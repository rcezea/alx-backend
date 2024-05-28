#!/usr/bin/env python3
""" Basic Flask Application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """ This routes to a basic template"""
    return render_template('0-index.html')
