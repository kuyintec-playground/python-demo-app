from __future__ import absolute_import
import os
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, static_folder='assets', static_url_path='')

@app.route('/', methods=['GET'])
def home():
    """ Home Page..
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = os.environ.get('FLASK_DEBUG', True)
    app.run(port=8080)
