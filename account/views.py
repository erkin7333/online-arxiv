from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import RegisterUserSerializer, LoginUserSerializer


class RegisterUser(APIView):
    """
    Foydalanuvchini tizimga kirish uchun ro'yxatdan o'tkazish uchun view
    fields = ['username', 'password',]
    """
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': "Malumot kiritilmadi...", 'data': serializer.data},
                            status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()
        return Response({'message': "Foydalanuvchi ro'yxatdan o'tkazildi"},
                        status=status.HTTP_201_CREATED)


class LoginUser(TokenObtainPairView):
    """
    Foydalanuvchini tizimga kirish uchun view
    fields = ['username', 'password']
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginUserSerializer

user_login_api_view = LoginUser.as_view()
