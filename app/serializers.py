from rest_framework import serializers
from .models import Label, Annotation,Document

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'title')

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('id', 'start', 'end', 'label', 'text')
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document 
        fields = ('id', 'content')        