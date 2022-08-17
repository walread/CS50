import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]
    holdings = db.execute("SELECT symbol, SUM(shares) AS shares_sum FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    total = cash

    for holding in holdings:
        info = lookup(holding["symbol"])
        db.execute("UPDATE transactions SET current_price = ? WHERE user_id = ? AND symbol = ?",
                   info["price"], user_id, holding["symbol"])
        total += info["price"] * holding["shares_sum"]

    holdings = db.execute(
        "SELECT symbol, name, SUM(shares) AS shares_sum, price, current_price, SUM(total) AS total_sum FROM transactions WHERE user_id = ? GROUP BY symbol HAVING shares_sum > 0", user_id)

    return render_template("index.html", holdings=holdings, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        symbol = request.form.get("symbol").upper()
        info = lookup(symbol)
        shares = request.form.get("shares")

        if not symbol:
            return apology("Missing symbol")

        elif not info:
            return apology("Invalid symbol")

        elif not shares:
            return apology("Missing shares")

        try:
            shares = int(shares)
        except:
            return apology("Invalid shares")

        if shares <= 0:
            return apology("Too few shares")

        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        name = info["name"]
        price = info["price"]
        total = price * shares

        if cash < total:
            return apology("Can't afford")

        else:
            db.execute("INSERT INTO transactions (user_id, symbol, name, shares, price, current_price, total, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       user_id, symbol, name, shares, price, price, total, "Bought")
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total, user_id)

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session["user_id"]

    holdings = db.execute("SELECT symbol, shares, price, type, time FROM transactions WHERE user_id = ?", user_id)

    return render_template("history.html", holdings=holdings)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Missing symbol")

        info = lookup(symbol)

        if not info:
            return apology("Invalid symbol")

        return render_template("quoted.html", info=info)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Missing username")

        elif not password:
            return apology("Missing password")

        elif len(password) < 10:
            return apology("Password must be at least 10 characters")

        elif not re.findall("[A-Z]", password):
            return apology("Password must contain at least one uppercase letter")

        elif not re.findall("[a-z]", password):
            return apology("Password must contain at least one lowercase letter")

        elif not re.findall("\d", password):
            return apology("Password must contain at least one number")

        elif not confirmation:
            return apology("Missing password confirmation")

        elif password != confirmation:
            return apology("Passwords do not match")

        elif len(db.execute("SELECT * FROM users WHERE username = ?", username)) != 0:
            return apology("Username is not avalible")

        hash = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)

        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        session["user_id"] = user[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session["user_id"]

    if request.method == "POST":

        symbol = request.form.get("symbol")
        info = lookup(symbol)
        shares = request.form.get("shares")

        if not symbol:
            return apology("Missing symbol")

        elif not shares:
            return apology("Missing shares")

        try:
            shares = int(shares)
        except:
            return apology("Invalid shares")

        if shares <= 0:
            return apology("Too few shares")

        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        name = info["name"]
        price = info["price"]
        total = price * shares
        current_shares = db.execute("SELECT SUM(shares) AS shares_sum FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",
                                    user_id, symbol)[0]["shares_sum"]

        if shares > current_shares:
            return apology("Attepmting to sell more shares than are owned")

        else:
            db.execute("INSERT INTO transactions (user_id, symbol, name, shares, price, current_price, total, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       user_id, symbol, name, -shares, price, price, -total, "Sold")
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + total, user_id)

        return redirect("/")

    else:

        holdings = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)

        return render_template("sell.html", holdings=holdings)
