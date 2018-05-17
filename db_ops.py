import sqlite3

db = sqlite3.connect("urls.db")
cursor = db.cursor()


def check_url(uri):
    """
    check whether a given hostname is in vulnerable urls db. If so it is considered unsafe to visit that url.
    :param uri: hostname
    :return: True if safe else false
    """
    original_url = uri.split('1/')[1].split('?')[0]
    hostname = original_url.split('/')[0].split(':')[0]
    safe = True
    urls = cursor.execute(
      "select url from url where url like ?",
      ('%' + hostname + '%',))
    results = urls.fetchall()
    if results:
        for result in results:
            if uri == result or hostname == result[0].split('/')[0] or uri == original_url:
                safe = False
    return safe
