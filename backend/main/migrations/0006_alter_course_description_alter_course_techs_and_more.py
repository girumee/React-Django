# Generated by Django 4.1.6 on 2023-02-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_course_featured_img_course_teacher_course_techs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='techs',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='interested_categories',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
