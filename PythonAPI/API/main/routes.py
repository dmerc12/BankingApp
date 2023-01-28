from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/customer/home")
def home():
    return render_template("home.html")
