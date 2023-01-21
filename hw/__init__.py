from flask import Flask, render_template, request
import requests as r

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=["GET", "POST"])
def pokemon():
    if request.method == "POST":
        pokemon_name = request.form["pokemon_name"]
        pokemon_data = findpokemon(pokemon_name)
        return render_template("pokemon_data.html", pokemon_data = pokemon_data)
    else:
        return render_template("pokemon.html")


if __name__ == '__main__':
    app.run(debug=True)