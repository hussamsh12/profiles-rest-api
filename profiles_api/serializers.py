from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing Hello APIView"""

    name = serializers.CharField(max_length=10, min_length=2)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=10)



class UserProfileSerializer(serializers.Serializer):
    """A Serializer for the User Profile"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, min_length=2, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=20, min_length=8, write_only=True, required=False)





class BuiltInUserProfileSerializer(serializers.ModelSerializer):
    """ A Serializer for the UserProfile"""
    class Meta:
        model = models.UserProfile

        fields = ('id', 'name', 'email', 'password')

        extra_kwargs = {
            'password': {
                "write_only": True,
                "style": {
                    "input_field": 'password'
                }
            }

        }


    def create(self, validated_data):
        """Creates a new user profile"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


    def update(self, instance, validated_data):
        """Updates the received User profile"""

        if 'password' in validated_data:
            password = validated_data['password']
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializer for the Profile Feed Item"""

    user_email = serializers.EmailField(source='user_profile.email', read_only=True)

    class Meta:
        model = models.ProfileFeedItem

        fields = ('id', 'user_profile', 'status_text', 'user_email', 'created_on')

        extra_kwargs = {
            'user_profile': {
                "read_only": True
            }
        }
