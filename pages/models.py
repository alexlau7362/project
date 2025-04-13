from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Page(models.Model):
    medium = models.CharField(max_length=50)
    admission_criteria = models.TextField(validators=[MaxLengthValidator(5000)])
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


    def __str__(self):
        return f"Course: {self.medium}"