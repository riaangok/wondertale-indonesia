import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure to use SQLite database
db = SQL("sqlite:///story.db")




@app.route("/sumatera")
def sumatera():

    return render_template("sumatera.html")

@app.route("/malin")
def malin():

    return render_template("malin.html")

@app.route("/danautoba")
def danautoba():

    return render_template("danautoba.html")

@app.route("/naimanggale")
def naimanggale():

    return render_template("naimanggale.html")

@app.route("/java")
def java():

    return render_template("java.html")

@app.route("/lutungkasarung")
def lutungkasarung():

    return render_template("lutungkasarung.html")

@app.route("/rorojonggrang")
def rorojonggrang():

    return render_template("rorojonggrang.html")

@app.route("/tangkubanperahu")
def tangkubanperahu():

    return render_template("tangkubanperahu.html")

@app.route("/sulawesi")
def sulawesi():

    return render_template("sulawesi.html")

@app.route("/Putri_Tandampalik")
def Putri_Tandampalik():

    return render_template("Putri_Tandampalik.html")

@app.route("/Batu_Bagga")
def Batu_Bagga():

    return render_template("Batu_Bagga.html")

@app.route("/Sigarlaki_and_Limbat")
def Sigarlaki_and_Limbat():

    return render_template("Sigarlaki_and_Limbat.html")

@app.route("/kalimantan")
def kalimantan():

    return render_template("kalimantan.html")

@app.route("/Batu_Menangis")
def Batu_Menangis():

    return render_template("Batu_Menangis.html")

@app.route("/Pangeran_Biawak_and_Putri_Bungsu")
def Pangeran_Biawak_and_Putri_Bungsu():

    return render_template("Pangeran_Biawak_and_Putri_Bungsu.html")

@app.route("/Asal_Usul_Danau_Lipan")
def Asal_Usul_Danau_Lipan():

    return render_template("Asal_Usul_Danau_Lipan.html")

@app.route("/papua")
def papua():

    return render_template("papua.html")

@app.route("/Empat_Raja")
def Empat_Raja():

    return render_template("Empat_Raja.html")

@app.route("/Asal_Usul_Irian")
def Asal_Usul_Irian():

    return render_template("Asal_Usul_Irian.html")

@app.route("/Asal_Usul_Burung_Cendrawasih")
def Asal_Usul_Burung_Cendrawasih():

    return render_template("Asal_Usul_Burung_Cendrawasih.html")

@app.route("/about")
def about():

    return render_template("about.html")

# adapted by finance #
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Sign Up user"""

    # forget any user_id
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ensure username was submitted
        if not username:
            # if the username is empty return apology
            return apology("The username is required", 400)

        # ensure password was submitted
        elif not password:
            # if the password is empty return apology
            return apology("The password field is required", 400)

        # ensure password-confirm was submitted
        elif not confirmation:
            # if the password-confirm is empty return apology
            return apology("The confirm password field is required", 400)

        # ensure password and password-confirm is match
        if password != confirmation:
            # if the password and password-confirm doesn't match return apology
            return apology("Sorry, passwords doesn't match", 400)

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        print(rows)

        # ensure that username already exist or not
        if len(rows) != 0:
            #     # if the username already exist return apology
            return apology("username is already exists", 400)

         # insert that username as a new user into database
        role = "user"
        db.execute("INSERT INTO users (username, password, role) VALUES(?, ?, ?)", username, generate_password_hash(password), role)

        # remember which user has log in
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]

        flash("Sign Up Successfully")

        # redirect user to home
        return redirect("/")
    else:
        return render_template("signup.html")

# adapted by finance #
@app.route("/signin", methods=["GET", "POST"])
def signin():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # user reached route via POST
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # ensure username was submitted
        if not username:
            return apology("The username is required", 403)

        # ensure password was submitted
        elif not password:
            return apology("The password field is required", 403)
        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], password):
            return apology("invalid username and/or password", 403)

        # remember which user has log in
        session["user_id"] = rows[0]["id"]

        flash("Welcome to Wondertale Indonesia")

        # redirect user to home
        return redirect("/")
    else:
        return render_template("signin.html")

# adapted by finance #
@app.route("/signout")
def signout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/")
def index():
    story = db.execute("SELECT * FROM stories")
    print(story)
    return render_template("index.html", story=story)

@app.route("/create")
@login_required
def create():
    """Form User Create Story"""

    return render_template("create.html")

@app.route("/save", methods=["GET", "POST"])
@login_required
def save():
    title = request.form.get("title")
    origin = request.form.get("origin")
    story = request.form.get("story")
    image = request.form.get("image")
    video = request.form.get("video")
    audio = request.form.get("audio")

    db.execute("INSERT INTO stories (title, origin, story, image, video, audio) VALUES(?, ?, ?, ?, ?, ?)", title, origin, story, image, video, audio)
    return redirect("/library")

@app.route("/library")
@login_required
def library():
    """Library User"""

    # Redirect user to login form
    return render_template("library.html")

@app.route("/timun_mas")
def timun_mas():
    story = db.execute("SELECT * FROM stories WHERE id=2")
    print(story)
    return render_template("timun_mas.html", story=story)
