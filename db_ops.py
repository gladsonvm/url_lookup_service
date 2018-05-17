import sqlite3

db = sqlite3.connect("urls.db")
cursor = db.cursor()


def check_url(hostname):
    """
    check whether a given hostname is in vulnerable urls db. If so it is considered unsafe to visit that url.
    :param hostname: hostname
    :return: True if safe else false
    """

    urls = cursor.execute(
      "select url from url where url like ?",
      ('%'+hostname+'%',))
    if urls.fetchone():
        return False
    return True
