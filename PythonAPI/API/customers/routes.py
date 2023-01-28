
from flask_bcrypt import Bcrypt
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user

from PythonAPI.API.customers.forms import LoginForm, RegistrationForm
from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.Entities.Customer import Customer
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

users = Blueprint('main', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated():
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Customer(customer_id=0, first_name=form.first_name.data, last_name=form.last_name.data,
                        username=form.username.data, password=hashed_password, email=form.email.data,
                        phone_number=form.phone_number.data, address=form.address.data)
        customer_sao.service_create_customer(user)
        flash('Your account has been created and you are now able to log in!', 'success')
        return redirect(url_for('users.login'))
    return render_template("register.html", title="Register", form=form)

@users.route("/")
@users.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = customer_sao.service_get_customer_by_email(email)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful, please check email and password!', 'danger')
    return render_template("login.html", title="Login", form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("users.login"))

@users.route("/manage/my/information")
def manage_customer_information():
    return render_template("manage_customer_information.html", title="Customer Information")

