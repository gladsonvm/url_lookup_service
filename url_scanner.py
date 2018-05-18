import random
import sqlite3


db = sqlite3.connect("urls.db")
cursor = db.cursor()


def scan_url(url):
    """
    if a given url is not in database check if it is vulnerable or
    not with info from some api calls or a public vulnerability database.
    As of now this method will randomly return True/False just to mock behavious
    :param url: url
    :return: True if not vulnerable else false
    """
    is_safe = random.choice([True, False])
    if is_safe:
        return True
    cursor.execute('insert into url (url) values (?)', (url,))
    return is_safe


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
    else:
        safe = scan_url(original_url)
    return safe



