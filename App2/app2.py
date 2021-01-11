from flask import Flask, render_template, url_for, request, redirect
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)
GoogleMaps(app)
@app.route('/')
def index():
    return render_template('index.html', mymap=mymap)

@app.route('/delete/')
def delete():
    return render_template("delete.html")

# @app.route('/', methods=['GET','PULL'])
# def getinputs():


if __name__ == '__main__':
    app.run(debug = True)
 
