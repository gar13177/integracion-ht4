from orchestrator.models import Promotion
from orchestrator.serializers import PromotionSerializer
from rest_framework import generics, status, mixins
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from orchestrator.apiendpoints.constants import Constants
from django.forms.models import model_to_dict
from orchestrator.externalcommunication.apicalls import requestPromotionsList


class PromotionsList(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()

    def get(self, request, *args, **kwargs):

        promotions = requestPromotionsList({'promotions': 'all'})
        print(promotions)
        if len(promotions) == 0:
            return Response(
                {
                    'message': Constants.ANSWER_NO_PROMOTIONS
                },
                status=status.HTTP_202_ACCEPTED
            )

        promotionsModels = []
        for promotion in promotions:
            promotionsModels.append(model_to_dict(Promotion(promotion)))

        return Response(
            promotionsModels,
            status=status.HTTP_202_ACCEPTED
        )
