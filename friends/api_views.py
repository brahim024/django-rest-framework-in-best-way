from rest_framework import viewsets
from .import models
from .import serializers

class FriendViewset(viewsets.ModelViewSet):
	queryset=models.Friend.object.all()
	serializer_class=serializers.FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
	queryset=models.Belonging.objetects.all()
	serializer_class=serializers.BelongingSerializer