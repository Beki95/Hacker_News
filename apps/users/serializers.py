from rest_framework import serializers as s
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User


class RegisterSerializer(s.ModelSerializer):
    password = s.CharField(max_length=50, min_length=8, write_only=True)
    user_name = s.CharField(min_length=2, max_length=15)

    class Meta:
        model = User
        fields = 'user_name', 'password'

    def validate(self, attrs):
        user_name = attrs.get('user_name')
        if User.objects.filter(user_name=user_name):
            raise ValidationError(
                {'user_name': 'That username is taken. Please choose another.'}
            )
        return attrs

    def create(self, validated_data):
        super(RegisterSerializer, self).create(validated_data)
        return validated_data

    def to_representation(self, instance):
        # give access_token for login
        data = super(RegisterSerializer, self).to_representation(instance)
        user = User.objects.filter(user_name=instance.get('user_name')).first()
        access = RefreshToken.for_user(user)
        data['access_token'] = str(access.access_token)
        return data


class UserProfileSerializer(s.ModelSerializer):
    password = s.CharField(write_only=True, min_length=8, max_length=50)
    password2 = s.CharField(write_only=True, min_length=8, max_length=50)
    user_name = s.CharField(read_only=True)

    class Meta:
        model = User
        fields = 'user_name', 'password', 'password2'

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise ValidationError({'password': "passwords don't match"})
        return attrs

    def update(self, instance, validated_data):
        password = validated_data.pop('password', False)
        if password:
            instance.set_password(raw_password=password)
        super(UserProfileSerializer, self).update(instance, validated_data)
        return validated_data
