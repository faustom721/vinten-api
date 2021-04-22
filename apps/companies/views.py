from rest_framework import viewsets
from apps.companies.models import Company, Membership
from apps.companies.serializers import CompanySerializer, MembershipSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MembershipViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        return Membership.objects.filter(user=user, active=True)
