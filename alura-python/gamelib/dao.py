from models import Game, User

SQL_DELETE_GAME = "delete from game where id = %s"
SQL_GAME_BY_ID = "SELECT id, name, category, console from game where id = %s"
SQL_USER_BY_ID = "SELECT id, name, password from user where id = %s"
SQL_UPDATE_GAME = "UPDATE game SET name=%s, category=%s, console=%s where id = %s"
SQL_SEARCH_GAMES = "SELECT id, name, category, console from game"
SQL_CREATE_GAME = "INSERT into game (name, category, console) values (%s, %s, %s)"


class GameDao:
    def __init__(self, db):
        self.__db = db

    def save_game(self, game):
        cursor = self.__db.connection.cursor()

        if game.id:
            cursor.execute(
                SQL_UPDATE_GAME, (game.name, game.category, game.console, game.id)
            )
        else:
            cursor.execute(SQL_CREATE_GAME, (game.name, game.category, game.console))
            game.id = cursor.lastrowid
        self.__db.connection.commit()
        return game

    def list_game(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SEARCH_GAMES)
        games = translate_games(cursor.fetchall())
        return games

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_GAME_BY_ID, (id,))
        game_tuple = cursor.fetchone()
        return Game(game_tuple[1], game_tuple[2], game_tuple[3], id=game_tuple[0])

    def delete_game(self, id):
        self.__db.connection.cursor().execute(SQL_DELETE_GAME, (id,))
        self.__db.connection.commit()


class UserDao:
    def __init__(self, db):
        self.__db = db

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USER_BY_ID, (id,))
        data = cursor.fetchone()
        user = translate_user(data) if data else None
        return user


def translate_games(games):
    def create_game_with_tuple(game_tuple):
        return Game(game_tuple[1], game_tuple[2], game_tuple[3], id=game_tuple[0])

    return list(map(create_game_with_tuple, games))


def translate_user(user_tuple):
    return User(user_tuple[0], user_tuple[1], user_tuple[2])
