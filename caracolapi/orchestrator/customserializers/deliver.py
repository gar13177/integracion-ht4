from rest_framework import serializers
from orchestrator.models import OrderUpdateRequest


class DeliverRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderUpdateRequest
        fiellds = ('order_token', 'order_state')
