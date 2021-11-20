import sqlite3


def get_tracks_duration():
    db = sqlite3.connect('example.sqlite3')
    cursor = db.cursor()

    cursor.execute("SELECT * from genres")
    duration_dict = {i[0]: [i[1], 0] for i in cursor.fetchall()}

    cursor.execute("SELECT GenreId, Milliseconds FROM tracks")
    for GenreId, Milliseconds in cursor.fetchall():
        duration_dict[GenreId][1] += Milliseconds

    db.close()
    return duration_dict


def top_hits(count):

    db = sqlite3.connect('example.sqlite3')
    cursor = db.cursor()

    cursor.execute("SELECT TrackId, Name from tracks")
    hits_dict = {i[0]: [i[1], 0] for i in cursor.fetchall()}

    cursor.execute("SELECT TrackId, UnitPrice, Quantity FROM invoice_items")
    for TrackId, UnitPrice, Quantity in cursor.fetchall():
        hits_dict[TrackId][1] += UnitPrice * Quantity

    db.close()

    hits_list = [i[1] for i in hits_dict.items()]

    if count:
        return sorted(hits_list, key=lambda _: _[1], reverse=True)[:count]
    else:
        return sorted(hits_list, key=lambda _: _[1], reverse=True)



