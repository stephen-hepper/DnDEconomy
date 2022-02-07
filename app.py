from flask import Flask, render_template, request, redirect, url_for


'''
Will handle the internet-facing side of things eventually (hopefully)
'''

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
