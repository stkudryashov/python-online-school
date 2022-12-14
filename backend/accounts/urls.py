from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import TokenVerifyView, UserInfoView


urlpatterns = [
  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),

  path('profile/', UserInfoView.as_view(), name='profile_data'),
]
