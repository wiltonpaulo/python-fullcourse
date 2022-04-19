import MySQLdb

print("Connecting...")
conn = MySQLdb.connect(
    user="root", passwd="Password_1983", host="mysql.wpstec.com", port=3306
)

# Uncomment if you want to recreate db...
conn.cursor().execute("DROP DATABASE `gamelib`;")
conn.commit()

create_tables = """SET NAMES utf8;
    CREATE DATABASE `gamelib` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `gamelib`;
    CREATE TABLE `game` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) COLLATE utf8_bin NOT NULL,
      `category` varchar(40) COLLATE utf8_bin NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `user` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `password` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"""

conn.cursor().execute(create_tables)

# inserting users
cursor = conn.cursor()
cursor.executemany(
    "INSERT INTO gamelib.user (id, name, password) VALUES (%s, %s, %s)",
    [
        ("wilton", "Wilton Paulo", "flask"),
        ("nico", "Nico", "7a1"),
        ("danilo", "Danilo", "vegas"),
    ],
)

cursor.execute("select * from gamelib.user")
print(" -------------  Users:  -------------")
for user in cursor.fetchall():
    print(user[1])

# inserting games
cursor.executemany(
    "INSERT INTO gamelib.game (name, category, console) VALUES (%s, %s, %s)",
    [
        ("God of War 4", "Action", "PS4"),
        ("NBA 2k18", "Sports", "Xbox One"),
        ("Rayman Legends", "Indie", "PS4"),
        ("Super Mario RPG", "RPG", "SNES"),
        ("Super Mario Kart", "Racer", "SNES"),
        ("Fire Emblem Echoes", "Strategy", "3DS"),
    ],
)

cursor.execute("select * from gamelib.game")
print(" -------------  Games:  -------------")
for game in cursor.fetchall():
    print(game[1])

# commiting changes
conn.commit()
cursor.close()
