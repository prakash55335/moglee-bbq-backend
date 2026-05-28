from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import AdminUser


def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access':  str(refresh.access_token),
    }


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens(user)
            return Response({
                'success': True,
                'message': 'User registered successfully.',
                'user':    UserSerializer(user).data,
                'tokens':  tokens,
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'errors':  serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user   = serializer.validated_data['user']
            tokens = get_tokens(user)
            return Response({
                'success': True,
                'message': 'Login successful.',
                'user':    UserSerializer(user).data,
                'tokens':  tokens,
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'errors':  serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            pass
        return Response({
            'success': True,
            'message': 'Logged out successfully.',
        }, status=status.HTTP_200_OK)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'success': True,
            'user':    UserSerializer(request.user).data,
        })