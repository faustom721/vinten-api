from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.people.models import CustomUser
from apps.people.serializers import UserSerializer, UserRegistrationSerializer


class UserViewSet(viewsets.ModelViewSet):
    # TODO: allow any only for creating user. For reading demand authentication. (sign up)
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, 200)
        except IntegrityError as e:
            print(e)
            return Response({'msg': 'username or ci in use'}, 400)


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def list(self, request):
        return Response(self.serializer_class(request.user).data, 200)
