from flask import Flask
import sys, os
import logging

app = Flask(__name__)
logging.basicConfig(filename="record.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadname)s : %(message)s')

@app.route('/hello')
def hello():
    return f"hi breakout 4"

@app.route('/registration')
def registration():
    return f"Welcome to registration room"


if __name__ == '__main__':
    app.run(port=3000, debug=True)    
