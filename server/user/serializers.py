from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)
    groups = serializers.StringRelatedField(many=True, read_only=True)
    group_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Group.objects.all(), source='groups', write_only=True, required=False
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                  'is_active', 'date_joined', 'groups', 'group_ids', 'profile']
        read_only_fields = ['date_joined']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        instance = super().update(instance, validated_data)
        
        if profile_data:
            UserProfile.objects.update_or_create(
                user=instance,
                defaults=profile_data
            )
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = UserProfileSerializer(required=False)
    group_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Group.objects.all(), source='groups', write_only=True, required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'group_ids', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        groups_data = validated_data.pop('groups', [])
        
        user = User.objects.create_user(**validated_data)
        
        if groups_data:
            user.groups.set(groups_data)
        
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        
        return user
