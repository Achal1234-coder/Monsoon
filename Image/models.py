from django.db import models
from Account.models import User
from ImageUploader.settings import MEDIA_ROOT

class Image(models.Model):
    id= models.BigAutoField(
                auto_created = True,
                unique=True,
                primary_key = True,
                serialize = False
                )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    descreption = models.TextField(null=True)
    image = models.ImageField(upload_to=MEDIA_ROOT)
    create_time = models.DateTimeField(auto_now_add=True)
