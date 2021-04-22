from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.people.models import CustomUser
from apps.people.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # TODO: allow any only for creating user. For reading demand authentication. (sign up)
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
