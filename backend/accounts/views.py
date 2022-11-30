from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

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

    def put(self, request):
        user_info, _ = UserInfo.objects.get_or_create(user=request.user)
        serializer = UserInfoSerializer(user_info, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
