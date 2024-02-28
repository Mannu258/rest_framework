from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from . serializers import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = studentserializers(student_objs,many=True)

#     return Response({'status':200,'payload':serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = studentserializers(data=request.data)
#     if not serializer.is_valid():
#         return Response({'status':403,"errors":serializer.errors,"messege":"somthing went wrong"})
#     serializer.save()
#     print(data)
#     return Response({'status':200,'payload':data,'messege':'your data is saved'})

# @api_view(['PUT'])
# def update_student(request,id):
#     try:

#         student_obj = Student.objects.get(id=id)
#         data = request.data
#         serializer = studentserializers(student_obj,data=request.data,partial=True)
#         if not serializer.is_valid():
#             return Response({'status':403,"errors":serializer.errors,"messege":"somthing went wrong"})
#         serializer.save()
#         print(data)
#     except Exception as e:
#         return Response({'status':403,'message':"invalid id"})
#     return Response({'status':200,'payload':data,'messege':'your data is saved'})

# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:

#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#     except Exception as e:
#         return Response({'status':403,'message':"invalid id"})
#     return Response({'status':200,'messege':'your data is Deleted'})








@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializers(book_objs,many=True)
    return Response({'status':200,'payload':serializer.data})


   

# @api_view(['POST'])
# def add_book(request):
#     try:
#         data = request.data
#         serializer = BookSerializers(data)
#         if not serializer.is_valid():
#             return Response({'status':403,"errors":serializer.errors,"messege":"somthing went wrong"})
#         serializer.save()
#         return Response({'status':200,'messege':'your data is Saved'})
#     except Exception as e:
#         print(e)


from rest_framework_simplejwt.tokens import RefreshToken

class studentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        student_objs = Student.objects.all()
        serializer = studentserializers(student_objs,many=True)
        return Response({'status':200,'payload':serializer.data})
    
    def post(self,request):
        data = request.data
        serializer = studentserializers(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,"errors":serializer.errors,"messege":"somthing went wrong"})
        serializer.save()
        print(data)
        return Response({'status':200,'payload':data,'messege':'your data is saved'})
    
    def patch(self,request):
        try:
            id = request.data['id']
            student_obj = Student.objects.get(id=id)
            data = request.data
            serializer = studentserializers(student_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({'status':403,"errors":serializer.errors,"messege":"somthing went wrong"})
            serializer.save()
            print(data)
        except Exception as e:
            return Response({'status':403,'message':"invalid id"})
        return Response({'status':200,'payload':data,'messege':'your data is saved'})

    def put(self,request): 
      pass
    def delete(self,request):
        try:
            id = request.data['id']
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
        except Exception as e:
            return Response({'status':403,'message':"invalid id"})
        return Response({'status':200,'messege':'your data is Deleted'})
    

class RegisterUser(APIView):
    def post(self,request):
        data=request.data
        serializer = UserSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,"errors":serializer.errors,"messege":"somthing went wrong"})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status':200,'refresh': str(refresh),
        'access': str(refresh.access_token),'payload':data,'messege':'Account Has been Created'})
    


from rest_framework import generics
class StudentGenric(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentserializers

class StudentGenric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = studentserializers
    lookup_field = "id"

class GenratePdf(APIView):
    def get(self,request):
        return Response({'status':200})