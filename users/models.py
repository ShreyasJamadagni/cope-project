from django.db import models

# Create your models here.
class UnregisteredUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.TextField()
    registration_code = models.TextField()

    def __str__(self):
        return self.registration_code
