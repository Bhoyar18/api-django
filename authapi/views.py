from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import MovieModel
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class MovieViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated]
    queryset =MovieModel.objects.all()
    serializer_class =MovieSerializer