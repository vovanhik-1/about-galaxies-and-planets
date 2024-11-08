import sqlite3

db = sqlite3.connect('database.db')


db.execute('''CREATE TABLE IF NOT EXISTS Satellites(
                satellites_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100) NOT NULL UNIQUE,
                img TEXT NOT NULL,
                description TEXT NOT NULL
                )''')


db.execute('''CREATE TABLE IF NOT EXISTS Planets(
                planet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100) NOT NULL UNIQUE,
                img TEXT NOT NULL,
                description TEXT NOT NULL,
                satellites_id INTEGER,
                FOREIGN KEY (satellites_id) REFERENCES Satellites(satellites_id) ON DELETE CASCADE
                )''')


db.execute('''CREATE TABLE IF NOT EXISTS Galaxies(
                galaxe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100) NOT NULL UNIQUE,
                img TEXT NOT NULL,
                description TEXT NOT NULL,
                planet_id INTEGER,
                FOREIGN KEY (planet_id) REFERENCES Planets(planet_id) ON DELETE CASCADE
                )''')

db.execute('''CREATE TABLE IF NOT EXISTS Exoplanets(
                exoplanet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100) NOT NULL UNIQUE,
                img TEXT NOT NULL,
                description TEXT NOT NULL,
                planet_id INTEGER,
                FOREIGN KEY (planet_id) REFERENCES Planets(planet_id) ON DELETE CASCADE
                )''')

# db.execute('''DELETE FROM Planets WHERE planet_id=10''')

# db.execute('''INSERT INTO Satellites (title, img, description)
#             VALUES ('Спутники Сатурна', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Saturn-map.jpg/250px-Saturn-map.jpg', 'Естественные спутники планеты Сатурн. По состоянию на июнь 2023 года у Сатурна известно 222 естественных спутников, открытие которых зарегистрировано Международным астрономическим союзом. Собственные названия имеют 63 спутника, остальные обозначаются номерами. Это наибольшее число открытых спутников среди всех планет Солнечной системы. Большинство спутников имеет небольшие размеры и состоят из каменных пород и льда. Они очень светлые, имеют высокую отражательную способность.')''')


# db.execute('''INSERT INTO Satellites (title, img, description)
#             VALUES ('Спутники Урана', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Uranus_moons.jpg/300px-Uranus_moons.jpg', 'Естественные спутники планеты Уран. По состоянию на 2024 год известно 28 спутников. Все они названы в честь персонажей произведений Уильяма Шекспира и Александра Поупа. Первые два спутника — Титанию и Оберон — открыл Уильям Гершель в 1787 году. Ещё два шарообразных спутника (Ариэль и Умбриэль) обнаружил в 1851 году Уильям Лассел. В 1948 году Джерард Койпер открыл Миранду. Остальные спутники были открыты после 1985 года, во время миссии «Вояджера-2» или с помощью сильных наземных телескопов.')''')


# db.execute('''INSERT INTO Satellites (title, img, description)
#             VALUES ('Спутники Нептуна, Ио, Европа, Ганимед, Каллисто', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/New_Webb_Images_Capture_Rare_View_of_Neptune%E2%80%99s_Rings_%28Labeled%29.png/350px-New_Webb_Images_Capture_Rare_View_of_Neptune%E2%80%99s_Rings_%28Labeled%29.png', 'естественные спутники планеты Нептун. По состоянию на 2024 год известно 16 таких спутников.')''')
# db.commit()


def select_galaxies():
    db = sqlite3.connect('database.db')
    galaxies = db.execute('''SELECT * FROM Galaxies''').fetchall()
    return galaxies

def select_planets():
    db = sqlite3.connect('database.db')
    planets = db.execute('''SELECT * FROM Planets''').fetchall()
    return planets

def select_satellites():
    db = sqlite3.connect('database.db')
    satellites = db.execute('''SELECT * FROM Satellites''').fetchall()
    return satellites

def select_Exoplanets():
    db = sqlite3.connect('database.db')
    exoplanets = db.execute('''SELECT * FROM Exoplanets''').fetchall()
    return exoplanets
