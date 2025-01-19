from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='category'),    # This will make serving on baseurl/first_app/       views defines like       views.<function_ka_name defined in views.py>
    path('<int:courseid>/', views.per_course, name='courseid'),  
]
