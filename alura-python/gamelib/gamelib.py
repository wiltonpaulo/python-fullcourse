from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash, url_for


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('God of War', 'Rack n Slash', 'PS2')
game3 = Game('Mortal Kombat', 'Fight', 'Mega Drive')
game_list = [game1, game2, game3]


class User:
    def __init__(self, name, nickname, password):
        self.name = name
        self.nickname = nickname
        self.password = password


user1 = User('wilton', 'wpsilva', 'flask/1010')
user2 = User('admin', 'adminuser', 'flask/1010')
user3 = User('joao', 'john', 'flask/1010')

users = {
    user1.nickname: user1,
    user2.nickname: user2,
    user3.nickname: user3
}


app = Flask(__name__)
app.secret_key = 'gamelib-secret'


@app.route('/')
def index():
    return render_template('list.html', title='Games', games=game_list)


@app.route('/new')
def new():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('new')))
    return render_template('new.html', title='New Game')


@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    game_list.append(game)
    return redirect(url_for('index'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['user'] in users:
        user = users[request.form['user']]
        if request.form['password'] == user.password:
            session['logged_user'] = user.nickname
            flash(user.nickname +
                  ' Successfully authenticated!', category='success')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash('Invalid username or password.', category='error')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logged out!', category='success')
    return redirect(url_for('index'))


app.run(debug=True, host='127.0.0.1', port=5000)
