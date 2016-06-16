from .utils import get_upload_token

from rest_framework.views import APIView
from rest_framework.response import Response
from enhancements.rest.urls import register_view


@register_view('uptoken/')
class UpTokenView(APIView):

    _ignore_model_permissions = True

    def get(self, request):
        return Response({
            'uptoken': get_upload_token()
        })
