from authapp.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password', }, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        try:
            validate_password(password=password, user=user)
        except ValidationError as e:
            raise serializers.ValidationError({'error': e.messages})

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user
