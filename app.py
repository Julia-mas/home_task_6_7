from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs
from db import get_tracks_duration, top_hits
from formater import dict_2_html, list_2_html

app = Flask(__name__)


@app.route('/tracks_duration')
def tracks_duration():
    return dict_2_html(get_tracks_duration())


@app.route('/best_sellers')
@use_kwargs(
    {
        'count': fields.Int(
            missing=None,
        )
    },
    location='query'
)
def top_tracks(count):
    return list_2_html(top_hits(count))


app.run(debug=True)
