from django.contrib.auth.models import User
from .models import Achievement, Blog, Event
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ( UserSerializer, AchievementSerializer, 
                           EventSerializer, BlogSerializer )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes # Django permission won't work with APIView


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]


@permission_classes((permissions.AllowAny,)) # This decorator to be used with APIView
class AchievementList(APIView):
    """
    List of all Achievements
    """

    def get(self, request, format=None):
        query = Achievement.objects.all()
        serializer = AchievementSerializer(query, many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,)) 
class EventList(APIView):
    """
    List of all Events
    """

    def get(self, request, format=None):
        query = Event.objects.all()
        serializer = EventSerializer(query, many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class BlogList(APIView):
    """
    List of all Blogs
    """

    def get(self, request, format=None):
        query = Blog.objects.all()
        serializer = BlogSerializer(query, many=True)
        return Response(serializer.data)

