from rest_framework import serializers
from orchestrator.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Django User Serializer
    """
    class Meta:
        model = User
        fields = ('url', 'id', 'username')

class LoginUserSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(vielw_name='snippet-highlight', format='html')
    user = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = LoginUser
        fields = ('user', 'password')

class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    #expiry = serializers.DateField(required=True)

    class Meta:
        model = AppUser
        fields = ('created', 'user_token', 'user_rights', 'expiry')

class OrderRequestedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderRequested
        fiellds = ('user_token', 'order')

class OrderStoredSerializer(serializers.HyperlinkedModelSerializer):
    user_token = serializers.ReadOnlyField(source='user_token.user_token')
    class Meta:
        model = OrderStored
        fields = ('created', 'user_token', 'order_token')