# Generated by Django 5.1.5 on 2025-01-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_rename_courses_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_category',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
        migrations.AddField(
            model_name='course_category',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]
