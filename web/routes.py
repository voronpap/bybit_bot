
from flask import render_template

def initialize_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/chart")
    def chart():
        return render_template("chart.html")
