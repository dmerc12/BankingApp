from flask import Blueprint, render_template

accounts = Blueprint('accounts', __name__)

@accounts.route("/analyze/transactions")
def view_transactions():
    return render_template("transactions.html", title="Transactions")

@accounts.route("/manage/my/accounts")
def manage_accounts():
    return render_template("manage_accounts.html", title="Accounts")
