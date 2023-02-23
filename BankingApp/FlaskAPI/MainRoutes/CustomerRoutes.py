import datetime

from flask import Blueprint, render_template, request, jsonify, current_app, make_response, redirect, url_for, flash, \
    session

from BankingApp.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from BankingApp.DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from BankingApp.Entities.FailedTransaction import FailedTransaction
from BankingApp.Entities.Session import Session
from BankingApp.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation
from BankingApp.SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

customer_routes = Blueprint("customer_routes", __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@customer_routes.route("/manage/customer", methods=["GET"])
def manage_customer():
    return render_template("Customer/ManageCustomer.html")

@customer_routes.route("/register", methods=["GET", "POST"])
def register():
    return render_template("Customer/Register.html")
