from rest_framework import  permissions , generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer

class PublicNoteListView(APIView):
    permission_classes = [permissions.AllowAny]
    

    def get(self, request, *args, **kwargs):
        notes = Note.objects.filter(owner=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
class ProtectedNoteCreateView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, *args, **kwargs):
        note_id = request.data.get('id')
        try:
            note = Note.objects.get(id=note_id, owner=request.user)
        except Note.DoesNotExist:
            return Response({'error': 'Note not found'}, status=404)

        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer