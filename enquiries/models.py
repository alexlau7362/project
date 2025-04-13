from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Enquiry(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    course_id = models.IntegerField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.course_id} {self.course}'
# Create your models here.


