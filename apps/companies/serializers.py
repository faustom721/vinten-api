from rest_framework import serializers
from apps.companies.models import Company, Membership


class CompanySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Company
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Membership
        fields = '__al__'
