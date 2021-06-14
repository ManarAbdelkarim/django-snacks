from django.db import models

# Create your models here.

class data_base(models.Model):
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    image = models.ImageField(upload_to='downloads')
    description = models.TextField(default = 'here is some description')

    def __str__(self):
        return self.user

