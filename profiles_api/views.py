from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from profiles_api import serializers, models, permissions
from profiles_api.models import UserProfile


class HelloAPIView(APIView):
    """an APIView that says Hello"""

    serializer_class = serializers.HelloSerializer

    def get(self, request):
        """Handles GET Methods to this APIView"""

        features = [                      #  Read, Create, Update,    delete
            "Uses HTTP methods as functions (GET, POST, PUT, PATCH, DELETE)",
            "Gives you control over the application logic",
            "Mapped manually by URLs"
        ]

        return Response({
            "message": "Hello",
            "features": features
        })

    def post(self, request):
        """Return a Hello message to the subscriber"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({"message": message})

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """Updates an object partially"""

        return Response({"message": request.method})

    def put(self, request, pk=None):
        """Updates the object fully"""
        return Response({"message": request.method})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({"message": request.method})



class HelloViewSet(viewsets.ViewSet):
    """Creates a Hello ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a Hello message"""
        features = [
            "Uses Actions (list, create, retrieve, update, partial_update, destroy)",
            "Provides functionality with less code",
            "Mapped Automatically using Routers"
        ]

        return Response({
            "message": "Hello",
            "features": features
        })


    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({"message": message})

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handles getting an object by its primary key"""
        return Response({"message": request.method})

    def update(self, request, pk=None):
        return Response({"message": request.method})


    def partial_update(self, request, pk=None):
        return Response({"message": request.method})

    def destroy(self,request, pk=None):
        return Response({"message": request.method})



# request
class UserProfileViewSet(viewsets.ViewSet):
    """View set for the User Profile"""

    serializer_class = serializers.UserProfileSerializer

    def list(self, request):
        """Return all users in our server"""

        users = models.UserProfile.objects.all()
        serializer = self.serializer_class(users, many=True)

        return Response(
            {"users": serializer.data},
            status.HTTP_200_OK

        )

    def create(self, request):
        """Creates a new user profile"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = models.UserProfile.objects.create_user(
                    name=name,
                    email=email,
                    password=password
                )

                return Response(
                    {'message': "Success",
                     'user_id': user.id
                     },
                    status.HTTP_200_OK

                )
            except Exception:
                return Response(
                    {'message': "Failed",
                     'Reason': 'Email already in use'
                     },
                    status.HTTP_400_BAD_REQUEST
                )

        return Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )


    def retrieve(self, request, pk=None):
        """Returns a user with primary key pk if exists"""
        try:
            user = models.UserProfile.objects.get(pk=pk)
            serializer = self.serializer_class(user)
            return Response(
                serializer.data,
                status.HTTP_200_OK

            )

        except UserProfile.DoesNotExist:
            return Response(
                {
                    'message': "Failed",
                    "Reason": "User with pk={} is not found".format(pk)
                },
                status.HTTP_400_BAD_REQUEST
            )


    def update(self, request, pk=None):
        """Updates a user profile in our server"""
        try:
            user = models.UserProfile.objects.get(pk=pk)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                name = serializer.validated_data['name']
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                user.name = name
                user.email = email
                user.set_password(password)
                user.save()
                return Response(
                    {
                        "message": "Successfully updated UserProfile"
                    },
                    status.HTTP_200_OK
                )
            return Response(

                serializer.errors
                ,
                status.HTTP_400_BAD_REQUEST
            )


        except UserProfile.DoesNotExist:
            return Response(
                {
                    'message': "Failed",
                    "Reason": "User with pk={} is not found".format(pk)
                },
                status.HTTP_400_BAD_REQUEST
            )


    def partial_update(self, request, pk=None):
        """Updates a profile partially"""
        try:
            user = models.UserProfile.objects.get(pk=pk)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                if 'name' in serializer.validated_data:
                    user.name = serializer.validated_data['name']
                if 'email' in serializer.validated_data:
                    user.email = serializer.validated_data['email']
                if 'password' in serializer.validated_data:
                    user.password = serializer.validated_data['password']
                user.save()
                return Response(
                    {
                        "message": "Successfully updated UserProfile"
                    },
                    status.HTTP_200_OK
                )
            return Response(

                serializer.errors
                ,
                status.HTTP_400_BAD_REQUEST
            )


        except UserProfile.DoesNotExist:
            return Response(
                {
                    'message': "Failed",
                    "Reason": "User with pk={} is not found".format(pk)
                },
                status.HTTP_400_BAD_REQUEST
            )



    def destroy(self, request, pk=None):
        try:
            user = models.UserProfile.objects.get(pk=pk)
            user.delete()
            return Response(
                {
                    "message": "Successfully deleted user"
                },
                status.HTTP_200_OK
            )
        except UserProfile.DoesNotExist:
            return Response(
                {
                    'message': "Failed",
                    "Reason": "User with pk={} is not found".format(pk)
                },
                status.HTTP_400_BAD_REQUEST
            )


class UserLoginAPIView(ObtainAuthToken):
    """Handles creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class BuiltInUserProfileViewSet(viewsets.ModelViewSet):
    """View Set for the User profile"""

    serializer_class = serializers.BuiltInUserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """A View set for the profile feed item"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

