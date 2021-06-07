from rest_framework import serializers
from apps.companies.models import Company, Membership, ExternalEntity
from apps.people.serializers import SimpleUserSerializer


class CompanySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Company
        fields = ('id', 'name', 'address', 'email', 'phone')


class MembershipSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    role = serializers.SerializerMethodField()

    class Meta(object):
        model = Membership
        fields = ('role', 'company', 'activity_description', 'user')

    def get_role(self, obj):
        return obj.get_role_display()


class ExternalEntitySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = ExternalEntity
        fields = '__all__'
