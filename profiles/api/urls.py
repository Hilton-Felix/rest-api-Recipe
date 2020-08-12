from django.urls import include, path
from .import views

urlpatterns = [
    path('create/', views.UserCreateAPIView.as_view(), name='create-user'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]