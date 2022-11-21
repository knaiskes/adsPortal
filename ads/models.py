from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
