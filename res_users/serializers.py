from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }
