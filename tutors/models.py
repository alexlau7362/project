# tutors/models.py
from django.db import models

class Tutor(models.Model):
    login_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('courses.Course',blank=True, related_name='tutors')  # Use string reference
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='tutors/%Y/%m/%d/', blank=True)
    admission_criteria = models.TextField(blank=True, default="Obtained Child-care Certificate")
    is_registered = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='enquiries')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name} for {self.course}"    

