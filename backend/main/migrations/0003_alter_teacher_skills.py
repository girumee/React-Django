# Generated by Django 4.1.6 on 2023-02-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='skills',
            field=models.TextField(max_length=100),
        ),
    ]
