from rest_framework import viewsets

from projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get("name", None)

        if name is not None:
            queryset = queryset.filter(name=name)

        return queryset
