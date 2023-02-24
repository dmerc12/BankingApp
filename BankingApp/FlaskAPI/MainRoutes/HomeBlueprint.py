from flask import Blueprint, render_template, session, flash, redirect, url_for

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

main_route = Blueprint("main_route", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@main_route.route("/home", methods=["GET"])
def home():
    if "session_id" not in session:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        return render_template("Main/Home.html")
