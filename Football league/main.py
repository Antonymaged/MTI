from flask import Flask, render_template, request, redirect, session
from sqlalchemy import text
from engine import engine

app = Flask(__name__)
app.config['SECRET_KEY'] = "SYNTAX CAN DO IT"

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/players')
def players():
    with engine.connect() as connection:
        query = text("SELECT * FROM players")
        result = connection.execute(query)
        rows = result.fetchall()

    return render_template("palyer-view-page.html", players=rows)

@app.route('/clubs')
def clubs():
    with engine.connect() as connection:
        query = text("SELECT * FROM clubs")
        result = connection.execute(query)
        rows = result.fetchall()

    return render_template("Club.html")

@app.route('/matches')
def matches():
    with engine.connect() as connection:
        query = text("SELECT * FROM matches")
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows:
            print(row)

    return render_template("matches.html", matches=rows)

@app.route('/league')
def league():
    with engine.connect() as connection:
        query = text("SELECT * FROM ltable")
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows:
            print(row)

    return render_template("league.html", league=rows)

@app.route('/club-info')
def club_info():
    team = request.args.get('team')
    with engine.connect() as connection:
        query = text("SELECT * FROM clubs WHERE cname = '{}'".format(team))
        result = connection.execute(query)
        rows = result.fetchone()
        for row in rows:
            print(row)

    return render_template("club-info.html", club=rows)

@app.route('/info-player')
def info_player():
    player = request.args.get('player')
    with engine.connect() as connection:
        query = text("SELECT * FROM players WHERE pname = '{}'".format(player))
        result = connection.execute(query)
        rows = result.fetchone()
        for row in rows:
            print(row)

    return render_template("info-player.html", player = rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)