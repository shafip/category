from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=200,
                            validators=[
                                RegexValidator(regex='^[a-zA-Z ]+$',
                                               message='Name must contain only letters and spaces.')])
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.Name


class SubCategory(models.Model):
    Category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    Field_Name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        value = f" {self.Category_name}"

        return value


from django.urls import reverse
from django.urls import reverse_lazy


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('cotable')

    def __str__(self):
        value = f" {self.course_name}"

        return value

    success_url = reverse_lazy('cotable')



class Topics(models.Model):
    courses_name = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    durations = models.IntegerField()
    topic = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class Subject(models.Model):
    name = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.CharField(max_length=30)
    subjects = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('topictable')
