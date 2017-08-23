from orchestrator.models import OrderStored
from orchestrator.serializers import DeliverRequestSerializer
from rest_framework import generics, status, mixins
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


class OrderUpdate(mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = DeliverRequestSerializer

    def post(self, request, *args, **kwargs):
        orderInfo = self.get_object()
        print(orderInfo)

        order = OrderStored.objects.get(order_token=orderInfo.order_token)
        # order.delete()
        return Response(order.data, status=status.HTTP_202_ACCEPTED)
