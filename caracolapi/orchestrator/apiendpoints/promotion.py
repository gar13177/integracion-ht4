#aqui va el endpoint
#el primero de login es el post y el segundo es un get
from orchestrator.externalcommunication.apicalls import requestPromotions
from orchestrator.models import Promotion
from orchestrator.serializers import PromotionSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
import json

class PromotionList(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    serializer_class = PromotionSerializer

    def get(self, request, *args, **kwargs):
        active_promotions = requestPromotions()
        promotions_to_display = []
        """for promo in active_promotions:
            print promo
            promotion_info = PromotionSerializer(active_promotions, many=True)
            promotions_to_display.append(promotion_info)
        """
        promotions_to_display = PromotionSerializer(active_promotions)
        return Response(promotions_to_display.data, status=status.HTTP_200_OK)
