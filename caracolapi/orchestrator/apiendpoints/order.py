from orchestrator.models import OrderRequested, OrderStored
from orchestrator.serializers import OrderRequestedSerializer, OrderStoredSerializer
from rest_framework import generics, status ,mixins
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework.response import Response

# ###########
from orchestrator.externalcommunication.apicalls import requestNewOrderToERP

class OrderRequestedList(mixins.CreateModelMixin,
                    generics.GenericAPIView):

    serializer_class = OrderRequestedSerializer

    def post(self, request, *args, **kwargs):
        # new order serializer
        new_order = OrderRequestedSerializer(data=request.data) 

        try:
            user = AppUser.objects.get(user_token=new_order['user_token'])
        except ObjectDoesNotExist:
            return Response({'user not found'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        order_billed = requestNewOrderToERP({
                request.data['order']
            })

        if order_billed['type'] != 'success':
            # error desde el request al ERP
            return Response({order_billed.errors}, status=status.HTTP_400_BAD_REQUEST)

        order_pending = sendOrderToProduction(order_billed)

        if order_pending['type'] != 'success':
            return Response({order_pending.errors}, status=status.HTTP_400_BAD_REQUEST)

        if order_pending['status'] == 'done':
            return Response(order_pending, status=status.HTTP_202_ACCEPTEDl)

        order = OrderStoredSerializer(order_pending)

        if auth_user.is_valid():
            order.save()
            return Response(order.data, status=status.HTTP_202_ACCEPTED)

        return Response(order.errors, status=status.HTTP_400_BAD_REQUEST)

class AppUserList(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class AppUserDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get(self, request, *args, **kwargs):
        try:
            db_user = AppUser.objects.get(user_token=kwargs['pk'])
            expire_date = db_user.expiry
            if timezone.now() > expire_date:
                db_user.delete()
        except ObjectDoesNotExist:
            pass
        return self.retrieve(request, *args, **kwargs)