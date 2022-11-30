from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import *
from accounts.models import UserInfo

from rest_framework.permissions import IsAuthenticated


class TokenVerifyView(APIView):
    """
    Получение данных пользователя по JWT Token
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_info, _ = UserInfo.objects.get_or_create(user=request.user)
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)
