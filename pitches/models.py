from django.db import models
from django.core.files import File
import os
from urllib.request import urlretrieve


class Pitch(models.Model):
    name = models.CharField(max_length=200)
    websiteURL = models.URLField(max_length=200)
    crunchbaseURL = models.URLField(max_length=200)
    videoURL = models.URLField(max_length=200)
    tags = models.CharField(max_length=200)
    companyID = models.CharField(max_length=200)
    pub_date = models.DateField()
    image_file = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name


