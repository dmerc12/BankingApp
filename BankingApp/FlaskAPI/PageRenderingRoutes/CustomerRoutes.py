from flask import Blueprint, render_template

customer_pages = Blueprint("customer_pages", __name__)

@customer_pages.route("/", methods=["GET"])
@customer_pages.route("/login", methods=["GET"])
def login():
    return render_template("Customer/Login.html")

@customer_pages.route("/home", methods=["GET"])
def home():
    return render_template("Main/Home.html")
