
def dict_2_html(param):

    res = '<h2>Duration of tracks sorted by genres in minutes:</h2>'
    for gr, ml in param.values():
        res += f'<b>{gr}</b>: {round(ml/60000,1)}<br>'
    return res


def list_2_html(param):

    res = f'<h2>Best sellers of tracks with invoice sum:</h2>'
    for tr_n, count in param:
        res += f'<b>{tr_n}</b>: {count}<br>'
    return res
