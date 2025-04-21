from django.db import models
from datetime import datetime
from tutors.models import Tutor
from . choices import location_choices, course_code_choices, course_name_choices
from django.core.validators import MaxLengthValidator

# Create your models here.
class Course(models.Model):
    # tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, default=1)
    
    tutor = models.ForeignKey(Tutor, on_delete=models.DO_NOTHING)
    course_name = models.CharField(max_length=200, choices=[(k, v) for k, v in course_name_choices.items()])
    course_code = models.CharField(max_length=20, choices=[(k, v) for k, v in course_code_choices.items()]) 
    # course_name = models.CharField(max_length=200, choices=course_name_choices.items())
    # course_code = models.CharField(max_length=20, choices=course_code_choices.items())
    medium = models.CharField(max_length=50)
    # tutor_name = models.CharField(max_length=50, choices=tutor_choices.items())
    admission_criteria = models.TextField(validators=[MaxLengthValidator(5000)])
    fee = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    parental_care = models.BooleanField()
    location = models.CharField(max_length=20, choices=[(k, v) for k, v in location_choices.items()], default="INDOOR")
    # location = models.CharField(max_length=7, choices=location_choices, default="INDOOR")
    class_size = models.IntegerField()
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f"Course: {self.course_name}"
    
