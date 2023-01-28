
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from PythonAPI.API import bcrypt, login_manager
from PythonAPI.API.customers.forms import LoginForm, RegistrationForm, RequestResetForm, ResetPasswordForm
from PythonAPI.API.customers.utils import send_reset_email, verify_reset_token
from PythonAPI.DAL.CustomerDAL.CustomerDALImplementation import CustomerDALImplementation
from PythonAPI.Entities.Customer import Customer
from PythonAPI.SAL.CustomerSAL.CustomerSALImplementation import CustomerSALImplementation

users = Blueprint('customers', __name__)

customer_dao = CustomerDALImplementation()
customer_sao = CustomerSALImplementation(customer_dao)

@login_manager.user_loader
def load_user(customer_id):
    user = customer_sao.service_get_customer_by_id(customer_id)
    return user

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        user = Customer(customer_id=0, first_name=register_form.first_name.data, last_name=register_form.last_name.data,
                        username=register_form.username.data, password=hashed_password, email=register_form.email.data,
                        phone_number=register_form.phone_number.data, address=register_form.address.data)
        customer_sao.service_create_customer(user)
        flash('Your account has been created and you are now able to log in!', 'success')
        return redirect(url_for('customers.login'))
    return render_template("register.html", title="Register", form=register_form)

@users.route("/")
@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = customer_sao.service_login(email, password)
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
    return redirect(url_for("customers.login"))

@users.route("/manage/my/information")
def manage_customer_information():
    return render_template("manage_customer_information.html", title="Customer Information")

@users.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        email = form.email.data
        user = customer_sao.service_get_customer_by_email(email)
        send_reset_email(user.email)
        flash("An email has been sent with instructions to reset your password.", "info")
        return redirect(url_for('customers.login'))
    return render_template("reset_request.html", title="Reset Password", form=form)

@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user = verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("customers.reset_request"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        current_info = customer_sao.service_get_customer_by_email(form.email.data)
        customer_sao.service_update_customer(Customer(current_info.customer_id, current_info.first_name,
                                                      current_info.last_name, current_info.username, hashed_password,
                                                      current_info.email,  current_info.phone_number,
                                                      current_info.address))
        flash("Your password has been updated! You are now able to log in", "success")
        return redirect(url_for("customers.login"))
    return render_template('reset_token.html', title='Reset Password', form=form)

