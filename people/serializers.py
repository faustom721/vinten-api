from rest_framework import serializers
from people.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = CustomUser
        fields = '__all__'
