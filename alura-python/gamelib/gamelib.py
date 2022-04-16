from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
from dao import GameDao, UserDao
from models import Game, User

app = Flask(__name__)
app.secret_key = "gamelib-secret"

app.config["MYSQL_HOST"] = "mysql.wpstec.com"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Password_1983"
app.config["MYSQL_DB"] = "gamelib"
app.config["MYSQL_PORT"] = 3306
db = MySQL(app)

game_dao = GameDao(db)
user_dao = UserDao(db)


@app.route("/")
def index():
    game_list = game_dao.list_game()
    return render_template("list.html", title="Games", games=game_list)


@app.route("/new")
def new():
    if "logged_user" not in session or session["logged_user"] == None:
        return redirect(url_for("login", next=url_for("new")))
    return render_template("new.html", title="New Game")


@app.route("/edit/<int:id>")
def edit(id):
    if "logged_user" not in session or session["logged_user"] == None:
        return redirect(url_for("login", next=url_for("edit")))
    game = game_dao.search_by_id(id)
    return render_template("edit.html", title="Edit Game", game=game)


@app.route("/delete/<int:id>")
def delete(id):
    game_dao.delete_game(id)
    flash("Game removed successfully!")
    return redirect(url_for("index"))


@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    category = request.form["category"]
    console = request.form["console"]
    game = Game(name, category, console)
    game_dao.save_game(game)
    return redirect(url_for("index"))


@app.route("/update", methods=["POST"])
def update():
    name = request.form["name"]
    category = request.form["category"]
    console = request.form["console"]
    game = Game(name, category, console, id=request.form["id"])
    game_dao.save_game(game)
    return redirect(url_for("index"))


@app.route("/login", methods=["POST", "GET"])
def login():
    next = request.args.get("next")
    return render_template("login.html", next=next)


@app.route("/signin", methods=["POST"])
def signin():
    user = user_dao.search_by_id(request.form["user"])
    if user:
        if user.password == request.form["password"]:
            session["logged_user"] = user.nickname
            flash(user.nickname + " Successfully authenticated!", category="success")
        next_page = request.form["next"]
        return redirect(next_page)
    else:
        flash("Invalid username or password.", category="error")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["logged_user"] = None
    flash("Logged out!", category="success")
    return redirect(url_for("index"))


app.run(debug=True, host="127.0.0.1", port=5000)
