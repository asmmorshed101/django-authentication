from rest_framework import serializers
from .models import Book, People, Color




class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        model = People
        # fields
        fields = '__all__'
        # depth = 1
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError("Age must be greater than or equal to 18")
        special_characters = "!@#$%^&*()_+-=[]{}|;':\",.<>/?`~"
        if any(char in special_characters for char in data['name']):
            raise serializers.ValidationError("Name should not contain special characters")
        return data
    
    # def validate_age(self, data):
    #     if data['age']<18:
    #         raise serializers.ValidationError("Age must be greater than or equal to 18")
    #     return data

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'