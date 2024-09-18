from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing Hello APIView"""

    name = serializers.CharField(max_length=10, min_length=2)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=10)
