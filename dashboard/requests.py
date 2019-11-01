import requests


def get_chvs():
    chvs = []
    base_url = 'http://127.0.0.1:8000'
    endpoint = 'api?query={chvs{id,age,phonenumber,location, profilePicture, }}'
    response = requests.get(base_url + '/' + endpoint)
    if response.status_code == 200:
        for data in response.json()['data']['chvs']:
            chvs.append(data)
        print(chvs)
        return chvs


def get_patients():
    patients = []
    base_url = 'http://127.0.0.1:8000'
    endpoint = 'api?query={patients{name, examiner{chv{name}}, age, gender, location, time, symptoms,urgency,actionTaken}}'
    response = requests.get(base_url + '/' + endpoint)
    if response.status_code == 200:
        for data in response.json()['data']['patients']:
            patients.append(data)
        print(patients)
        return patients


def get_emergencies():
    emergencies = []
    base_url = 'http://127.0.0.1:8000'
    endpoint = 'api?query={emergencies{type, reportedBy{chv{name}}}}'
    response = requests.get(base_url + '/' + endpoint)
    if response.status_code == 200:
        for data in response.json()['data']['emergencies']:
            emergencies.append(data)
        print(emergencies)
        return emergencies


def get_locations():
    locations = []
    base_url = 'http://127.0.0.1:8000'
    endpoint = 'api?query={locations{name,county,accessibility}}'
    response = requests.get(base_url + '/' + endpoint)
    if response.status_code == 200:
        for data in response.json()['data']['locations']:
            locations.append(data)
        print(locations)
        return locations
