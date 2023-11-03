from rest_framework import serializers
from Register_Login.models import Profile
from  django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class LocationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['Location',]
    
    def update(self, instance, validated_data):
        instance.Location = validated_data.get('Location', instance.Location)
        instance.save()
        return instance




class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )
