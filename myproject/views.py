from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from myproject.serializers import UserSerializer
from rest_framework import generics


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAuthToken(APIView):
    """
    Get products
    username -- Username
    password -- Password
    """
    # ANY USER
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        # the password verified for the user
        if user.is_active:
          token, created = Token.objects.get_or_create(user=user)
          request.session['auth'] = token.key
          return redirect('/users', request)
      return redirect(settings.LOGIN_URL, request)
