from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

punteggio_sosp = 0
punteggio_rass = 0


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)