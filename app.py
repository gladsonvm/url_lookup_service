from twisted.web import server, resource
from twisted.internet import reactor, endpoints
from response import Response
from utils import extract_data


class HttpHandler(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        request.setHeader(b"content-type", b"application/json")
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        return Response.response(Response(request, data=extract_data(request)))

endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(HttpHandler()))
reactor.run()




