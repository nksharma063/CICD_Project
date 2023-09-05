from flask import Flask
import sys, os
<<<<<<< HEAD
<<<<<<< HEAD

app = Flask(__name__)
=======
import logging
=======
import logging

app = Flask(__name__)
logging.basicConfig(filename="record_app.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
>>>>>>> 0831f26 (Add: new fucntions, updated .gitignore file and some logging fucntions, also testig the pipeline)

app = Flask(__name__)
logging.basicConfig(filename="record_app.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

>>>>>>> 0831f26 (Add: new fucntions, updated .gitignore file and some logging fucntions, also testig the pipeline)
@app.route('/hello')
def hello():
    return f"hi breakout 4"

@app.route('/registration')
def registration():
    return f"Welcome to registration room"

<<<<<<< HEAD
=======
@app.route('/aboutus')
def aboutus():
    return f"Welcome to about us page"

@app.route('/aboutus')
def aboutus():
    return f"Welcome to about us page"

@app.route('/error')
def error():
    app.logger.error(f'erro1')
    app.logger.info(f'info1')
    app.logger.critical(f'detail1')
    return f'Loggin error page'
<<<<<<< HEAD
>>>>>>> 0831f26 (Add: new fucntions, updated .gitignore file and some logging fucntions, also testig the pipeline)
=======
>>>>>>> 0831f26 (Add: new fucntions, updated .gitignore file and some logging fucntions, also testig the pipeline)

if __name__ == '__main__':
    app.run(port=3000, debug=True)