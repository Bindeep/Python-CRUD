import requests

parameters = {
    'name': ''
}

resp = requests.get('https://localhost/home')

if resp.status_code != 200:
    raise resp.ApiError('error occured')