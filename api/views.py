from django.http import Http404
from django.shortcuts import render
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegister,UserDataSerializer
from rest_framework.authtoken.models import Token
from  rest_framework.permissions import IsAuthenticated


# Create your views here.
class registerapi(APIView):
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create= Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)

class welcome(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)

class userdetails(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except:
           raise Http404
    def get(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDataSerializer(userData)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDataSerializer(userData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':'error','error':serializer.errors})
    def delete(self,request,pk,format=None):
        userData=self.get_object(pk)
        userData.delete()
        return Response({'message':'user deleted'})
