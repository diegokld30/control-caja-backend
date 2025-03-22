# apps/users/api/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.users.models import User
from apps.users.api.serializer import (
    UserRegisterSerializer,
    UserSerializer,
    UserUpdateSerializer
)

# Para registrar usuarios nuevos (abierto a cualquier usuario)
class RegisterUserViewSet(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

# Para consultar o actualizar el usuario autenticado (me)
class UserMeView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UserUpdateSerializer
        return UserSerializer

# Para operaciones generales con usuarios
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
