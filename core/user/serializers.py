from core.user.models import User,Profile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'phone_no', 'last_name', 'is_active', 'created', 'updated']
        read_only_fields = ['is_active', 'created', 'updated']
        


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_image', 'user_bio', 'premium']
        read_only_fields=['premium']