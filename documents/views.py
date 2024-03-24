from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

from .serializers import *


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = Photo.objects.all()
        category = self.request.query_params.get('category', None)

        if category is not None:
            queryset = queryset.filter(category=category)

        return queryset
