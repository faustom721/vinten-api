from rest_framework import viewsets
from people.models import CustomUser, Role
from people.serializers import UserSerializer, RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [IsOwnerOrIsValidMethod]
    # lookup_url_kwarg = 'id'


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
