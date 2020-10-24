#Tacorico787
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete/')
def delete():
    return render_template("delete.html")


if __name__ == '__main__':
    app.run('localhost', 5000)
