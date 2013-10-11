#from django.conf import settings
from models import RequestLog
from datetime import datetime


class HttpRequestLoggingMiddleware(object):

    """ Middleware that stores http requests to db """

    def process_request(self, request):
        httprequest = RequestLog(date=datetime.now(),
                                 method=request.method,
                                 url=request.path,
                                 query_str=request.META.get("QUERY_STRING"))
        httprequest.save()
