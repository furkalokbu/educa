from rest_framework import generics
from ..models import Subject
from ..serializers import SubjectSerializer


class SubjectlistView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializers_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializers_class = SubjectSerializer
