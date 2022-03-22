from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserSerializer, UpdateUserSerializer


class CreateUserAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GetOrUpdateOrDeleteSingleUserAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PATCH", "PUT"]:
            return UpdateUserSerializer
        return UserSerializer
