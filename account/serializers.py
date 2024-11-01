from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterUserSerializer(serializers.ModelSerializer):
    """Foydalanuvchi ro'yxatdan o'tish uchun"""
    class Meta:
        model = User
        fields = ('username', 'password')


class LoginUserSerializer(TokenObtainPairSerializer):
    """
    Ro'yxatdan o'tgan foydalanuvchilarni tizimga kirish uchun login serializer
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['id'] = self.user.id
        data['is_director'] = self.user.is_director
        data['is_archivist'] = self.user.is_archivist
        data['is_download'] = self.user.is_download
        return data