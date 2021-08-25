from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Project


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        projects = Project.objects.order_by("-pub_date")
        return render(request, self.template_name, {"projects": projects})


class ProjectView(TemplateView):
    template_name = "project.html"

    def get(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(name_text=kwargs.get("project_name"))
        except Project.DoesNotExist:
            raise Http404("Project does not exist")
        return render(request, self.template_name, {"project": project})
