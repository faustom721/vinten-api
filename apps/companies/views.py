from django.db.models import query
from rest_framework import viewsets
from apps.companies import serializers
from apps.companies.models import Company, Membership, Client
from apps.companies.serializers import CompanySerializer, MembershipSerializer, ExternalEntitySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MembershipViewSet(viewsets.ModelViewSet):
    """ Logged in user's memberships """

    # turn off pagination
    pagination_class = None
    serializer_class = MembershipSerializer

    def get_queryset(self):
        return Membership.objects.filter(user=self.request.user, is_active=True)


class ClientViewSet(viewsets.ModelViewSet):
    """ Logged in user's company's clients """

    serializer_class = ExternalEntitySerializer

    def get_queryset(self):
        # company_id is a path param of this endpoint
        return Client.objects.filter(company=self.kwargs.get('company_id'))
