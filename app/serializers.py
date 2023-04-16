from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ContactModel

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20, min_length=4)
    last_name = serializers.CharField(max_length=20, min_length=4)
    username = serializers.CharField(max_length=10, min_length=4)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100, min_length=8)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['id','first_name','last_name','country_code','phone','is_favourite']

