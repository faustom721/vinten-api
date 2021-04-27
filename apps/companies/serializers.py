from rest_framework import serializers
from apps.companies.models import Company, Membership


class CompanySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Company
        fields = ('name', 'address', 'email', 'phone')


class MembershipSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta(object):
        model = Membership
        fields = ('role', 'company', 'activity_description')
