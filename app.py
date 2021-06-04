from flask import Flask
from flask import request
from flask import render_template

import sqlite3
from sqlite3 import Error

app = Flask(__name__)

if __name__ == '__main__':
    app.run()