from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import Course_Category

def home(request):
    categories = Course_Category.objects.all()
    return render(request, 'website/index.html', {'categories': categories})


