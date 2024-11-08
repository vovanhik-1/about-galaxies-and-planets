from flask import Flask, render_template
from database import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html' )


@app.route('/planets')
def planet():
    planets = select_planets()
    exoplanets = select_Exoplanets()
    return render_template('planets.html', planets=planets, exoplanets=exoplanets)


@app.route('/satellites')
def satellit():
    satellites = select_satellites()
    return render_template('satellit.html', satellites=satellites)



@app.route('/galaxy')
def galaxy():
    galaxies = select_galaxies()
    return render_template('galaxies.html', galaxies=galaxies )








if __name__ == '__main__':
    app.run(debug=True)
