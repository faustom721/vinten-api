from django.db.models import query
from rest_framework import viewsets
from apps.companies import serializers
from apps.companies.models import Company, Membership, Client
from apps.companies.serializers import CompanySerializer, MembershipSerializer, ExternalEntitySerializer
from utils import get_request_company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MembershipViewSet(viewsets.ModelViewSet):
    """ Logged in user's memberships """

    serializer_class = MembershipSerializer

    def get_queryset(self):
        return Membership.objects.filter(user=self.request.user, is_active=True)


class ClientViewSet(viewsets.ModelViewSet):
    """ Logged in user's company's clients """

    serializer_class = ExternalEntitySerializer

    def get_queryset(self):
        company = get_request_company(self.request)
        return Client.objects.filter(company=company)
