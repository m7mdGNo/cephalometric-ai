from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Landmark(models.Model):
    image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='landmarks')
    name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return self.name