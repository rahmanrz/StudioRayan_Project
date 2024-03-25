from django.db import models


# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects')

    def __str__(self):
        return self.title
