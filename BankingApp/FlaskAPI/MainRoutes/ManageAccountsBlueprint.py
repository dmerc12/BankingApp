from flask import Blueprint, render_template, redirect, url_for, flash, session

account_routes = Blueprint("account_routes", __name__)

@account_routes.route("/manage/accounts", methods=["GET"])
def manage_accounts():
    if "session_id" not in session:
        flash(message="Please log in!", category="error")
        return redirect(url_for("login_route.login"))
    else:
        return render_template("Account/ManageAccounts.html")
