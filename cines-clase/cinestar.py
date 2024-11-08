from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cines", defaults={'id': None})
@app.route("/cines/<id>")
def cines (id):
    if id == None :
        data= requests.get('https://oaemdl.es/cinestar_sweb_php/cines')
        cines  = data.json()['data']
        return render_template('cines.html', cines = cines)
    cine = None
    return render_template('cines.html', cine = cine)


@app.route("/peliculas/<id>")
def peliculas(id):
    peliculas = None
    return render_template('peliculas.html', peliculas = peliculas)

if __name__ == "__main__" :
    app.run(debug=False)