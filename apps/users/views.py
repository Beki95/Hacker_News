from rest_framework import generics

# Create your views here.
from apps.users.models import User
from apps.users.serializers import RegisterSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


register = RegisterView.as_view()


class UserProfile(generics.ListAPIView,
                  generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


profile = UserProfile.as_view()
