from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from re import *

from .models import Notes
from .serializers import NotesSerializer, UserSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = []

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        pattern_email = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        is_valid_email = pattern_email.match(username)

        if user:
            if is_valid_email:
                return Response(
                    {
                        "token": user.auth_token.key,
                        "username": user.username
                    }
                )
            else:
                return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class NoteList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        notes = Notes.objects.filter(author=request.user)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        data['author'] = request.user.id
        serializer = NotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotesDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NotesSerializer(note)
        if note.author == request.user:
            return Response(serializer.data)
        else:
            return Response({"error": "This article does not belong to this user"}, 
                            status=status.HTTP_400_BAD_REQUEST)
            

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        data = request.data
        data['author'] = request.user.id
        serializer = NotesSerializer(note, data=data)
        if serializer.is_valid():
            if note.author == request.user:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"error": "This article does not belong to this user"}, 
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        if note.author == request.user:
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            Response({"error": "This article does not belong to this user"}, 
                     status=status.HTTP_400_BAD_REQUEST)