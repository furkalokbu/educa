from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import (
    BaseAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import detail_route, permission_classes

from ..models import Subject, Course
from .permissions import IsEnrolled
from .serializers import (
    SubjectSerializer,
    CourseSerializer,
    CourseWithContentsSerializer,
)


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# class CourseEnrollView(APIView):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled'})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @detail_route(
        methods=["GET"],
        serializer_class=CourseWithContentsSerializer,
        authentication_classes=[BasicAuthentication],
        permission_classes=[IsAuthenticated, IsEnrolled],
    )
    # def enroll(self, request, *args, **kwargs):
    #     course = self.get_object()
    #     course.students.add(request.user)
    #     return Response({'enrolled': True})
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
