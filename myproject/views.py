from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
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
  #ANY USER
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

# class Users1(APIView):
#     """
#     View to list all users in the system.

#     * Requires session authentication.
#     * Only admin users are able to access this view.
#     """
#     # ONLY Admin user
#     # authentication_classes = (authentication.SessionAuthentication,)
#     # permission_classes = (permissions.IsAdminUser,)

#     # Any logged in user
#     # authentication_classes = (authentication.SessionAuthentication,)
#     # permission_classes = (permissions.IsAuthenticated,)

#     # ANY USER
#     authentication_classes = ()
#     permission_classes = ()

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)

#     def get_auth_token(request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # the password verified for the user
#             if user.is_active:
#                 token, created = Token.objects.get_or_create(user=user)
#                 request.session['auth'] = token.key
#                 return redirect('/users', request)
#         return redirect(settings.LOGIN_URL, request)
