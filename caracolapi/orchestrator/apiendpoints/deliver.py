from orchestrator.models import OrderStored
from orchestrator.serializers import DeliverRequestSerializer
from rest_framework import generics, status, mixins
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from orchestrator.apiendpoints.constants import *


class OrderUpdate(mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = DeliverRequestSerializer

    def post(self, request, *args, **kwargs):
        try:
            order = OrderStored.objects.get(order_token=request.data['order_token'])
        except OrderStored.DoesNotExist:
            order = None

        if order is None:
            return Response(
                {
                    'errors': ANSWER_ORDER_NOT_FOUND
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.data['order_state'] == ORDER_DELIVERED:
            order.delete()
            return Response(
                {
                    'message': ANSWER_DELIVER_SUCCESS
                },
                status=status.HTTP_202_ACCEPTED
            )

        order.status = request.data['order_state']
        order.save()

        return Response(
            {
                'message': ANSWER_ORDER_UPDATE_SUCCESS
            },
            status=status.HTTP_202_ACCEPTED
        )
