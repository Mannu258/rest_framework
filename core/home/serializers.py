from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User


class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude = ['id']
        fields = '__all__'
    def validate(self , data):
        if data['age']<18 and data['age']<80:
            raise serializers.ValidationError({'error':"age cannot be less the 18"})
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':"cannot use digit in name"})

        return data

class CateogerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Cateogry
        # fields = '__all__'
        fields = ['Cateogry_name']


class BookSerializers(serializers.ModelSerializer):
    cateogry = CateogerySerializers() # here you can add specific field like which paraticulur do you want
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1 you can add but if you want the all field in serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self,validate_data):
        user = User.objects.create(username=validate_data['username'])
        password = validate_data['password']
        user.set_password(password)
        user.save()
        return user

        
