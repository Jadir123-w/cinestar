from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cines", defaults={'id': None})
@app.route("/cines/<id>")
def cines(id):
    if id is None:
        data = requests.get('https://oaemdl.es/cinestar_sweb_php/cines')
        cines = data.json().get('data', [])
        return render_template('cines.html', cines=cines)
    
    data_cine = requests.get(f'https://oaemdl.es/cinestar_sweb_php/cines/{id}')
    data_tarifas = requests.get(f'https://oaemdl.es/cinestar_sweb_php/cines/{id}/tarifas')
    cine = data_cine.json().get('data', {})
    tarifas = data_tarifas.json().get('data', [])
    return render_template('cine.html', cine=cine, tarifas=tarifas)

@app.route("/peliculas", defaults={'id': None})
@app.route("/peliculas/<id>")
def peliculas(id):
    if id is None:
        data = requests.get('https://oaemdl.es/cinestar_sweb_php/peliculas')
        peliculas = data.json().get('data', [])
        return render_template('peliculas.html', peliculas=peliculas)
    
    data = requests.get(f'https://oaemdl.es/cinestar_sweb_php/peliculas/{id}')
    pelicula = data.json().get('data', {})
    return render_template('pelicula.html', pelicula=pelicula)

@app.route("/peliculas/cartelera")
def cartelera():
    data = requests.get('https://oaemdl.es/cinestar_sweb_php/peliculas/cartelera')
    cartelera = data.json().get('data', [])
    return render_template('peliculas.html', peliculas=cartelera)

if __name__ == "__main__":
    app.run(debug=False)
