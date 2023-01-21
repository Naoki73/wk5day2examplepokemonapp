from app import app
from flask import Flask, render_template, request
import requests as r


def findpokemon(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = r.get(url)
    if response.ok:
        my_dict = response.json()
        pokemon_dict = {}
        pokemon_dict["Name"] = my_dict["name"]
        pokemon_dict["Ability"] = my_dict["abilities"][0]["ability"]["name"]
        pokemon_dict["Front_Shiny"] = my_dict["sprites"]["front_shiny"]
        pokemon_dict["Base_ATK"] = my_dict["stats"][1]["base_stat"]
        pokemon_dict["Base_HP"] = my_dict["stats"][0]["base_stat"]
        pokemon_dict["Base_DEF"] = my_dict["stats"][2]["base_stat"]
        return pokemon_dict
    else:
        return "The pokemon you're looking for does not exist."


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