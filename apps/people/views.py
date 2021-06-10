from apps.companies.models import Membership
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.people.models import CustomUser
from apps.people.serializers import UserSerializer, UserRegistrationSerializer
from apps.companies.models import Membership


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


class SetLastUsedCompanyView(APIView):

    def post(self, request):
        company = request.data.get('company')
        # set the corresponding membership (the user-company relationship) to last_used=true
        membership = Membership.objects.filter(
            user=request.user, company__pk=company).first()

        if membership:
            membership.last_used = True
            membership.save()
            return Response(status=200)
        else:
            return Response(status=404)
