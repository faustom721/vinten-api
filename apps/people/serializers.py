from rest_framework import serializers
from apps.people.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = CustomUser
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name',
                  'password', 'password2', ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            is_tutor=self.validated_data['is_tutor'],
            is_student=self.validated_data['is_student'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
