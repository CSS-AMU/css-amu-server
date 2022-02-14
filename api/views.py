from django.contrib.auth.models import User
from .models import Achievement, Event, Member, Publication
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ( UserSerializer, AchievementSerializer,
                           EventSerializer, PublicationSerializer, MemberSerializer )
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
        query = Event.objects.all().order_by('-date')
        serializer = EventSerializer(query, many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class PublicationList(APIView):
    """
    List of all Blogs
    """

    def get(self, request, format=None):
        query = Publication.objects.all().order_by('-date')
        serializer = PublicationSerializer(query, many=True)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class MemberListView(APIView):
    """
    List of all Blogs
    """

    def post(self,request,*args,**kwargs):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
