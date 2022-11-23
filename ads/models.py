from django.db import models

class Type(models.Model):
    ad_type_text = models.CharField(max_length=25)

    def __str__(self):
        return self.ad_type_text

class Ad(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published')
    ad_type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
