from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

from views.index import *

if __name__ == '__main__':
    app.run(debug=True)