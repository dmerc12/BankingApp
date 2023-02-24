from flask import Blueprint, render_template, flash, session, redirect, url_for

transaction_routes = Blueprint("transaction_routes", __name__)

@transaction_routes.route("/analyzing transactions", methods=["GET"])
def analyze_transactions():
    if "session_id" not in session:
        flash("Please log in!")
        return redirect(url_for("login_route.login"))
    else:
        return render_template("Transaction/Transactions.html")
