from django.shortcuts import render
from first_app.models import Course_Category
from django.shortcuts import get_object_or_404

# Create your views here.

# This will make serving on baseurl/first_app/
def all_categories(request):
    return render(request, 'first_app/all_categories.html')




def per_course(request, courseid):
    course = get_object_or_404(Course_Category, pk = courseid)
    return render(request, 'first_app/per_course.html', {'course': course})