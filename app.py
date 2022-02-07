from flask import Flask, render_template, request, redirect, url_for


'''
Will handle the internet-facing side of things eventually (hopefully)
'''

app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello_world():  # put application's code here
    return render_template('Home.html')

@app.route('/brelor',methods=['GET','POST'])
def show_brelor_table():
    return render_template('brelor.html')


@app.route('/gottstand',methods=['GET','POST'])
def show_gottstand_table():  # put application's code here
    return render_template('gottstand.html')


if __name__ == '__main__':
    app.run()
