from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views


urlpatterns = [
    url(r'^api/list-users/$', views.OrganizerUserViewSet.as_view(), name='user-list'),
    url(r'^api/users/?$', views.RegistrationAPIView.as_view()),
    url(r'^api-auth/(?P<user_mail>.+)/$', views.OrganizerUserItemView.as_view(), name='user-detail'),
    url(r'^api/jwt-auth/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
]