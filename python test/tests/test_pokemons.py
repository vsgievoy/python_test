import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3e61135cde3e259c873e30baf7ec4cdc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 23241

def test_status_code ():
    response = requests.get (url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name ():
    response_new = requests.get (url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_new.json()["data"][0]["trainer_name"] == 'Вовчик'