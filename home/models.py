from django.db import models

# Create your models here.
class Querie(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.message
