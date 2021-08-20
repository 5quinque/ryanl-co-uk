# from django.shortcuts import render

# from django.http import HttpResponse

# def homePageView(request):
#     return HttpResponse('Hello, World!')

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'