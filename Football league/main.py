from flask import Flask,render_template, request, redirect, session
from engine import engine
from sqlalchemy import text

app = Flask(__name__)
app.config['SECRET_KEY'] = "SYNTAX CAN DO IT";
connection = engine.connect()

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
    

connection.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)