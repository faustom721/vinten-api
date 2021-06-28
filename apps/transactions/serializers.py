from rest_framework import serializers
from apps.transactions.models import ExternalEntity, Income, Outcome


class IncomeSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Income
        fields = '__al__'


class OutcomeSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Outcome
        fields = '__al__'
