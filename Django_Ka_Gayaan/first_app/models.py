from django.db import models
from django.utils import timezone

# Create your models here.

class Course_Category(models.Model):
  COURSE_CATEGORY = [
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('React', 'React'),
    ('Angular', 'Angular'),
    ('Vue', 'Vue'),
    ('Nodejs', 'Nodejs'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='courses/')                # for uploading image
  image2 = models.ImageField(upload_to='courses/', blank=True, null=True)  # optional second image
  image3 = models.ImageField(upload_to='courses/', blank=True, null=True)  # optional third image
  date_added = models.DateTimeField(default=timezone.now)
  category = models.CharField(max_length=8, choices=COURSE_CATEGORY, default='Python')
  category_description = models.TextField(max_length=500, blank=True, null=True)
  price = models.IntegerField(default=100)

  def __str__(self):
    return self.name