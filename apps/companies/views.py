from rest_framework import viewsets
from apps.companies.models import Company, Membership
from apps.companies.serializers import CompanySerializer, MembershipSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MembershipViewSet(viewsets.ModelViewSet):
    """ Logged in user's memberships """

    serializer_class = MembershipSerializer

    def get_queryset(self):
        return Membership.objects.filter(user=self.request.user, active=True)
