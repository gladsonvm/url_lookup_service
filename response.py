import datetime
import json


class Response(object):
    """
    Response formatter class.
    """
    def __init__(self, request, data=None):
        self.request = request
        self.data = data if data else None

    def response(self):
        """
        adds meta info to response dict and converts it to json
        :return: response as json
        """
        resp = dict()
        resp['meta'] = {
            'resource_uri': self.request.uri,
            'timestamp': str(datetime.datetime.utcnow())
        }
        resp.update(self.data)
        return json.dumps(resp)
