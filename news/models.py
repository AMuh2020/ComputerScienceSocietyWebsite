from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    link = models.URLField(max_length=100)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title