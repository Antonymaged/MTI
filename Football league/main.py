from flask import Flask, render_template
from sqlalchemy import create_engine, text
from engine import engine

app = Flask(__name__)
app.config['SECRET_KEY'] = "SYNTAX CAN DO IT"

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/players')
def players():
    with engine.connect() as connection:
        query = text("SELECT * FROM players")
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows:
            print(row)

    return render_template("players.html")

@app.route('/clubs')
def clubs():
    with engine.connect() as connection:
        query = text("SELECT * FROM clubs")
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows:
            print(row)

    return render_template("clubs.html")

@app.route('/matches')
def matches():
    with engine.connect() as connection:
        query = text("SELECT * FROM matches")
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows:
            print(row)

    return render_template("matches.html")

@app.route('/league')
def league():
    with engine.connect() as connection:
        query = text("SELECT * FROM league")
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows:
            print(row)

    return render_template("league.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)