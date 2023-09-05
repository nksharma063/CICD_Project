from flask import Flask
import sys, os
import logging

app = Flask(__name__)
logging.basicConfig(filename="record_app.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/hello')
def hello():
    return f"hi breakout 4"

@app.route('/registration')
def registration():
    return f"Welcome to registration room and will do add some content later"

@app.route('/aboutus')
def aboutus():
    return f"Welcome to about us page"

@app.route('/error')
def error():
    app.logger.error(f'erro1')
    app.logger.info(f'info1')
    app.logger.critical(f'detail1')
    return f'Loggin error page'

if __name__ == '__main__':
    app.run(port=3000, debug=True)