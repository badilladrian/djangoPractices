from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Form, Choice, Input


class InputSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Input 
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    inputs = InputSerializer(many=True, required=False)
    class Meta: 
        model = Choice 
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer): 
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta: 
        model = Form 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data): 
        user = User( 
            email=validated_data['email'], 
            username=validated_data['username'] 
            ) 
        user.set_password(validated_data['password']) 
        user.save() 
        Token.objects.create(user=user) 
        return user
