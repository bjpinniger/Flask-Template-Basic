from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, json, session
from app import app
from .forms import ExampleForm
import pprint as pp
from config import Config

app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY


# - - - Routes - - -

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
