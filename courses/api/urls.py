from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("subject/", views.SubjectlistView.as_view(), name="subject_list"),
    path("subject/<pk>/", views.SubjectDetailView.as_view(), name="subject_detail"),
]