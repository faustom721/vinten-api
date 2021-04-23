from rest_framework import serializers
from apps.people.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = CustomUser
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'ci', 'email', 'first_name', 'last_name',
                  'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        print(self.validated_data.get('ci'))
        user = CustomUser.objects.create_user(
            username=self.validated_data.get('username'),
            ci=self.validated_data.get('ci'),
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            password=self.validated_data.get('password'),
            email=self.validated_data.get('email'),
            phone=self.validated_data.get('phone')
        )
