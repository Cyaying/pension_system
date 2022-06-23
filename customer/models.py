from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    GENDER = (
        (0, "Male"),
        (1, "Female"),
    )
    TYPE = (
        (0, "Admin"),
        (1, "Elder")
    )
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=20, blank=False)
    sex = models.SmallIntegerField(choices=GENDER, default=0)
    age = models.SmallIntegerField(default=60)
    phone_number = models.CharField(max_length=20)
    identity_number = models.CharField(max_length=30)
    room_id = models.SmallIntegerField()
    register_time = models.DateTimeField(default=timezone.now)
    type = models.SmallIntegerField(choices=TYPE, default=1)
    
    def __str__(self):
        return self.name
