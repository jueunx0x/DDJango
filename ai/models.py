from django.db import models

# Create your models here.
class Image(models.Model):
        title = models.CharField(max_length=500)
        imagefile = models.FileField(upload_to="ai/image", null=True)
        def __str__(self):
            return self.title