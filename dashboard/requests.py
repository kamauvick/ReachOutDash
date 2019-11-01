import requests


def get_chvs():
    chvs = []
    BASE_URL = 'http://127.0.0.1:8000'
    ENDPOINT = 'api?query={chvs{id,age,phonenumber,location}}'
    response = requests.get('https://vicknwatch.herokuapp.com/api/')
    if response.status_code == 200:
        for data in response.json():
            chvs.append(data)
        print(chvs)
        return chvs
