from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Custom_User(AbstractUser):
    ROLE_CHOICES = (
    ('superuser','Superuser'),
    ('teacher','Teacher'),
    ('student','Student'),
)
    role = models.CharField(max_length=10 , choices=ROLE_CHOICES , default = 'student')
    birth_date = models.DateField(null = True , blank = True)

    def __str__(self):
        return self.username
    
    


