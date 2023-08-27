from flask import Flask
import sys, os

app = Flask(__name__)
@app.route('/hello')
def hello():
    return f"hi breakout 4"

@app.route('/registration')
def registration():
    return f"Welcome to registration room"


if __name__ == '__main__':
    app.run(port=3000, debug=True)    
