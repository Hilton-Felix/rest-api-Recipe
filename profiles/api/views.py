from rest_framework import generics

from profiles.models import User

from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated

# Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . serializers import AuthTokenSerializer


# support for User manager
from rest_framework import authentication, permissions


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ IsAuthenticated ]
    


# Create Token View
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



# manage authenticated user
class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [ IsAuthenticated ]


    def get_object(self):
        return self.request.user


