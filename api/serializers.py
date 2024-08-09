
from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=50)
#     email=serializers.EmailField()
#     city=serializers.CharField(max_length=50)

# def create(self, validated_data):
#         return Student.objects.create(**validated_data)

# def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id","name","email","city"]