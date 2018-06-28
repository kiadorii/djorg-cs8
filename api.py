from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content')

class NoteViewSet(viewsets.ModelViewSet):
    querySet = Note.objects.all()