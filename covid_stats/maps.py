import json

from urllib.request import urlopen


def cyprus_map():
    with urlopen(
            'https://raw.githubusercontent.com/cploutarchou/covid-19-tracker-django-app/master/data-sources/cyprus'
            '.geojson') as response:
        cyprus = json.load(response)
