from flask import Flask
import sys, os
from flask import logging

app = Flask(__name__)
logging.basicConfig(filename="record_app.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadname)s : %(message)s')

@app.route('/hello')
def hello():
    return f"hi breakout 4"

@app.route('/registration')
def registration():
    return f"Welcome to registration room and will do add some content later"

@app.route('/error')
def error():
    logger.error(f'erro1')
    logger.info(f'info1')
    logger.critical(f'detail1')

if __name__ == '__main__':
    app.run(port=3000, debug=True)    
