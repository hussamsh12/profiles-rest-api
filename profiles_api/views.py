from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers



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




