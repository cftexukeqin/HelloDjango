from django.shortcuts import render
from . import models


def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog2/index.html', {"article": article})
