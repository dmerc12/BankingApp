from flask import Blueprint, render_template

customer_routes = Blueprint("customer_routes", __name__)

@customer_routes.route("/", methods=["GET"])
@customer_routes.route("/login", methods=["GET"])
def login():
    return render_template("Customer/Login.html")

@customer_routes.route("/home", methods=["GET"])
def home():
    return render_template("Main/Home.html")

@customer_routes.route("/manage/customer", methods=["GET"])
def manage_customer():
    return render_template("Customer/ManageCustomer.html")
