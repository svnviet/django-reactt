from .models import Blog
from rest_framework import viewsets
from .serializers import FilmSerializers
from rest_framework.permissions import IsAuthenticated


class FilmApiView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = FilmSerializers
    permission_classes = [IsAuthenticated, ]
