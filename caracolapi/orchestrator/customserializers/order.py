from rest_framework import serializers
from orchestrator.models import *

class OrderRequestedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderRequested
        fields = ('user_token', 'order')

class OrderStoredSerializer(serializers.HyperlinkedModelSerializer):
    user_token = serializers.ReadOnlyField(source='user_token.user_token')
    class Meta:
        model = OrderStored
        fields = ('created', 'user_token', 'order_token', 'status')