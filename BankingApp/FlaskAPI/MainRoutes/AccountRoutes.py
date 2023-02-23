from flask import Blueprint, render_template

account_routes = Blueprint("account_routes", __name__)

@account_routes.route("/manage/accounts", methods=["GET"])
def manage_accounts():
    return render_template("Account/ManageAccounts.html")
