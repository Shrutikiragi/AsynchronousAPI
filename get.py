from flask import request

from Hello import app


def show_the_login_form():
    pass


def do_the_login():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()