# -*- coding: utf-8 -*-
"""
Peyton Yen
py2259
Final
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/1006")
def hello():
    return render_template("index.html")

#start the server
if __name__ == "__main__":
    app.run()