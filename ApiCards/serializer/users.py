from rest_framework import serializers
from ..models.user import user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields= ['id','name','email','authId']
        read_only = ['created_at',]

class AdminUserSerializer(serializers.ModelSerializer):
    is_superuser = serializers.SerializerMethodField()

    class Meta:
        model = user
        fields = ['id','name','email','authId','is_superuser']
    def get_is_superuser(self, obj):
        return obj.user_type == 1