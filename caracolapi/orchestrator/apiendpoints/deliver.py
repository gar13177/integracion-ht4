from orchestrator.models import OrderStored
from orchestrator.serializers import DeliverRequestSerializer
from rest_framework import generics, status ,mixins
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


class LoginUserList(mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = DeliverRequestSerializer

    def post(self, request, *args, **kwargs):
        orderInfo = self.get_object()
        try:
            order = OrderStored.objects.get(order_token=orderInfo.order_token)
            # order.delete()
            return Response(auth_user.data, status=status.HTTP_202_ACCEPTED)
        except ObjectDoesNotExist:
            pass

        auth_user = AppUserSerializer(data=user_info)
        if auth_user.is_valid():
            auth_user.save()
            return Response(auth_user.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(auth_user.errors, status=status.HTTP_400_BAD_REQUEST)
