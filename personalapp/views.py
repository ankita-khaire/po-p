from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Note
from .models import Account
from .serializers import NoteSerializer
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes((AllowAny,))
def Registration_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="successfully registered new user."
            data['email']=account.email
            data['username']=account.username
        else:
            data=serializer.errors
        return Response(data)     

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


                    
# Create your views here.

@permission_classes((IsAuthenticated,))
class NoteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):  
        notes=Note.objects.all()
        serializer=NoteSerializer(notes, many=True)
        return Response(serializer.data)  

    def post(self,request):  
        serializer=NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)            

class NoteDetails(APIView):
    def get_object(self,id):
        try:
            return Note.objects.get(id=id)

        except Note.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        note=self.get_object(id)
        serializer=NoteSerializer(note) 
        return Response(serializer.data)

    def put(self,request,id):
        note=self.get_object(id)
        serializer=NoteSerializer(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):  
        note=self.get_object(id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
