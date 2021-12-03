from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=64, min_length=7)

    class Meta:
        fields = "__all__"

class extendeduser(serializers.Serializer):
    class Meta:
        fields = "__all__"
    