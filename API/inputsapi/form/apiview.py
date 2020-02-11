#This is using the APIview from the REST Framework 
#from rest_framework.views import APIView
#from rest_framework.response import Response 
from rest_framework import generics 
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .models import * 
from .serializers import *

#For authentication
from django.contrib.auth import authenticate

class LoginView(APIView): 
    permission_classes = ()

    def post(self, request,): 
        username = request.data.get("username") 
        password = request.data.get("password") 
        user = authenticate(username=username, password=password) 
        if user: 
            return Response({"token": user.auth_token.key}) 
        else: 
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class FormList(generics.ListCreateAPIView):
    queryset = Form.objects.all() 
    serializer_class = FormSerializer


class FormDetail(generics.RetrieveDestroyAPIView): 
    queryset = Form.objects.all() 
    serializer_class = FormSerializer


class ChoiceList(generics.ListCreateAPIView): 
    def get_queryset(self): 
        queryset = Choice.objects.filter(form_id=self.kwargs["pk"]) 
        
        return queryset 
    serializer_class = ChoiceSerializer


class CreateInput(APIView):
    def post(self, request, pk, choice_pk): 
        filled_by = request.data.get("filled_by") 

        data = {'choice': choice_pk, 'form': pk, 'filled_by': filled_by} 
        serializer = InputSerializer(data=data) 
        
        if serializer.is_valid(): 
            input = serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FormViewSet(viewsets.ModelViewSet): 
    queryset = Form.objects.all() 
    serializer_class = FormSerializer


class UserCreate(generics.CreateAPIView): 
    authentication_classes = (TokenAuthentication) 
    permission_classes = () 
    serializer_class = UserSerializer