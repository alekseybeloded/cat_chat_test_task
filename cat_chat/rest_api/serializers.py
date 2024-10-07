from cat.models import Cat
from django.contrib.auth.models import User
from rest_framework import serializers


class CatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cat
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['username'],)
        user.set_password(validated_data['password'])
        user.save()
        return user
