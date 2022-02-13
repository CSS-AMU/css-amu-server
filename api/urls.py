from django.urls import include, path
from rest_framework import routers
from .views import (UserViewSet, AchievementList, EventList, PublicationList, MemberListView)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('achievements/',AchievementList.as_view(),name='achievement'),
    path('events/',EventList.as_view(),name='event'),
    path('publications/',PublicationList.as_view(),name='publication'),
    path('join/',MemberListView.as_view(),name='join'),
]