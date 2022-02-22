from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Achievement, Member, Publication, Event

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
        fields = ['title','img','description','date']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['author','details','date']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name','email','course','enrollment']