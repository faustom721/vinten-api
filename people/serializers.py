from rest_framework import serializers
from people.models import CustomUser, Role


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = CustomUser
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Role
        fields = '__al__'
