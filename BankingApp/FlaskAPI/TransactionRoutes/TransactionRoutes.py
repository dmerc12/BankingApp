from flask import Blueprint, render_template

transaction_routes = Blueprint("transaction_routes", __name__)

@transaction_routes.route("/analyzing transactions", methods=["GET"])
def analyze_transactions():
    return render_template("Transaction/Transactions.html")
