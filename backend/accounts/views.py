from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import *

from rest_framework.permissions import IsAuthenticated


class TokenVerifyView(APIView):
    """
    Получение данных пользователя по JWT Token
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
