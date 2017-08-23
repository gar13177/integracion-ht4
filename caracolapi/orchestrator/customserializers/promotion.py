from rest_framework import serializers
from orchestrator.models import Promotion


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = ('promotion_description', 'promotion_expiration_date')
