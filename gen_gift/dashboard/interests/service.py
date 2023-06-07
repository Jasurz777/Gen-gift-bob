import requests
import requests
import requests


def get_teachers():
    url = 'https://fintechhub.herokuapp.com/api/v1/teacher/'

    response = requests.get(url)
    return response.json()



