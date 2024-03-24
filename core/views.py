from datetime import timedelta

import djoser.views
from djoser import utils
from djoser.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response

from bizsite.settings import is_development, to_bool
from .models import SiteSettings
from .serializers import SiteSettingsSerializer


is_localhost = to_bool(is_development)


class SiteSettingsViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSettingsSerializer
    queryset = SiteSettings.objects.all()


class TokenCreateView(djoser.views.TokenCreateView):
    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = settings.SERIALIZERS.token

        response = Response()
        data = token_serializer_class(token).data

        response.set_cookie(
            key = "access_token",
            value = data["auth_token"],
            max_age = timedelta(days=30),
            secure = not is_localhost,
            httponly = True,
            samesite = "Lax",
            domain = "finleysg.pythonanywhere.com" if not is_localhost else None,
        )

        response.data = "Welcome!"
        response.status_code = status.HTTP_200_OK
        return response


class TokenDestroyView(djoser.views.TokenDestroyView):
    """Use this endpoint to logout user (remove user authentication token)."""

    permission_classes = settings.PERMISSIONS.token_destroy

    def post(self, request):
        response = Response()
        response.delete_cookie("access_token")
        response.status_code = status.HTTP_204_NO_CONTENT
        utils.logout_user(request)
        return response