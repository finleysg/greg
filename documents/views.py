from rest_framework import viewsets, permissions, pagination
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

from .serializers import *


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        doc_type = self.request.query_params.get('type', None)

        if doc_type is not None:
            queryset = queryset.filter(document_type=doc_type)

        return queryset


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = Photo.objects.all()
        tags = self.request.query_params.get('tags', None)

        if tags is not None and tags != "":
            tag_set = tags.split(",")
            for tag in tag_set:
                queryset = queryset.filter(tags__tag__name__icontains=tag)

        queryset = queryset.order_by("-last_update")
        return queryset


@api_view(("GET",))
@permission_classes((permissions.AllowAny,))
def random_photos(request):
    try:
        tag = request.query_params.get("tag", None)
        take = request.query_params.get("take", "1")
        photo = Photo.objects.random(tag, int(take))
        serializer = PhotoSerializer(photo, context={"request": request}, many=True)
        return Response(serializer.data)
    except:
        return Response(status=204)
