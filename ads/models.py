from django.db import models

class Type(models.Model):
    ad_type_text = models.CharField(max_length=25)

    def __str__(self):
        return self.ad_type_text

class Ad(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.CharField(max_length=25, default='0')
    ad_type = models.ForeignKey(Type, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
