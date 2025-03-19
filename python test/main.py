import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3e61135cde3e259c873e30baf7ec4cdc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_new_pokemon = {
    "name": "Пикачу",
    "photo_id": 1
}
body_change_name = {
    "pokemon_id": "270931",
    "name": "KamazMaster",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "270930"
}
new_pokemon = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_new_pokemon)
print(new_pokemon.text)

change_name = requests.put (url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(change_name.text)

pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print = (pokeball.text)