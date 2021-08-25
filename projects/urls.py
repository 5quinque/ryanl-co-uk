from django.urls import path

from .views import IndexView, ProjectView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("project/<str:project_name>/", ProjectView.as_view(), name="View"),
]
