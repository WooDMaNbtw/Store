from django import http
from corsheaders.middleware import CorsMiddleware
from rest_framework.response import Response
from rest_framework.views import APIView


class CorsCustomMiddleware(CorsMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (request.method == "OPTIONS"  and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META):
            response = http.HttpResponse()
            response["Content-Length"] = "0"
            response["Access-Control-Max-Age"] = 86400
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE, GET, OPTIONS, PATCH, POST, PUT"
        response["Access-Control-Allow-Headers"] = "*"

        return response


class CorsBaseAPIView(APIView):
    """
    Base API view with common options method
    """
    def options(self, request, *args, **kwargs):
        """
        Handle OPTIONS requests
        """
        # Customize the allowed methods based on your requirements
        headers: dict | None = {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        }
        return Response(status=200, data=None, headers=headers)