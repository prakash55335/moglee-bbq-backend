from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import AdminUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = AdminUser
        fields = ['username', 'full_name', 'role', 'password']

    def create(self, validated_data):
        return AdminUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid username or password.')
        if not user.is_active:
            raise serializers.ValidationError('Account is disabled.')
        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['id', 'username', 'full_name', 'role', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']