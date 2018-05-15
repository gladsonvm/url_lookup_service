

def extract_data(request):
    """
    extract required data from request url and return a dict with same.
    :param request: WSGI request
    :return: dict with hostname, port and original url
    """
    return {
        'hostname': request.uri.split('/')[2].split(':')[0],
        'port': request.uri.split('/')[2].split(':')[1],
        'original_path': '/'.join(request.uri.split('/')[2:])
    }

