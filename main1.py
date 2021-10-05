
from flask import Flask, request
from multiprocessing.pool import ThreadPool


app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page running'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)