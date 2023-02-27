from django.db import models

# teacher model


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=bool)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    skills = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "1. Teachers"

    def __str__(self):
        return self.full_name

# Course Category Model


class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "2. Course Categories"

    def __str__(self):
        return self.title

# Course Model


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    featured_img = models.ImageField(upload_to='course_imgs/', null=True)
    techs = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "3. Courses"

# Teacher Model


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=bool)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField(null=True)
    interested_categories = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "4. Students"
