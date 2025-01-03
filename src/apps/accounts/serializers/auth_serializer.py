from rest_framework import serializers

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    phone = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()