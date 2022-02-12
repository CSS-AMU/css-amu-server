from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Achievement, Blog, Event

class UserSerializer(serializers.ModelSerializer):
    staff_of = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email','staff_of']


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['name','description']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name','img','description']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','link']