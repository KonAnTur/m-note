from django.http import Http404

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Notes
from .serializers import NotesSerializer

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
            raise Http404('No such note found')

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