from flask import render_template
from comunidadeclp import app




@app.route('/')
def home():
    return render_template('home.html')


