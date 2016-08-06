from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    """
    User registration serializer
    """
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=200)
