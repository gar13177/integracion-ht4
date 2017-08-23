from orchestrator.models import OrderStored
from orchestrator.serializers import DeliverRequestSerializer
from rest_framework import generics, status, mixins
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


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
                    'errors': 'No se encontro la orden'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.data['order_status'] == 'entregado':
            order.delete()
            return Response(
                {
                    'message': 'Orden entregada correctamente'
                },
                status=status.HTTP_202_ACCEPTED
            )

        order.status = request.data['order_status']
        order.save()

        return Response(order, status=status.HTTP_202_ACCEPTED)
