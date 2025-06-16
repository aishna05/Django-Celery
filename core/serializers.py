from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User
from rest_framework import serializers
from .tasks import send_welcome_email

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'owner', 'created_at']
        # read_only_fields = ['owner']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        send_welcome_email.delay(user.email)
        return user
    
