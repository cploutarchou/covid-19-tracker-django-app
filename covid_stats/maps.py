import json
from urllib.request import urlopen

import plotly.graph_objs as go
from plotly.offline import plot


def cyprus_map():
    with urlopen(
            'https://raw.githubusercontent.com/cploutarchou/covid-19-tracker-django-app/master/data-sources/cyprus'
            '.json') as response:
        cyprus = json.load(response)

        fig = go.Figure(
            go.Choroplethmapbox(
                geojson=cyprus,
                colorscale=[[0, '#FFFAF4'], [.005, '#FFE4CC'], [.030, '#DC654F'], [.060, '#CA3328'], [.080, '#B80000'],
                            [.100, '#7C100C'], [.150, '#580000'], [.175, '#300000'], [1, '#170707']]
            )
        )

        fig.update_layout(
            mapbox_style='carto-positron',
            paper_bgcolor='rgba(0,0,0,0)',


            mapbox_zoom=2.75,
            mapbox_center={'lat': 37.0902, 'lon': -95.7129},
            margin=dict(t=0, l=0, r=0, b=0)
        )
        plot_div = plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})

        return plot_div
