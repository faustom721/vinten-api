from rest_framework import serializers
from transactions.models import ExternalEntity, Income, Outcome


class ExternalEntitySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = ExternalEntity
        fields = '__al__'


class IncomeSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Income
        fields = '__al__'


class OutcomeSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Outcome
        fields = '__al__'
