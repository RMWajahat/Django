from django.shortcuts import render

# Create your views here.

# This will make serving on baseurl/first_app/
def all_categories(request):
    return render(request, 'first_app/all_categories.html')