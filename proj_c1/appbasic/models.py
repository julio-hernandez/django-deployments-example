from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileModel(models.Model):
    basic_user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics_dir', blank=True)

    def __str__(self):
        return self.basic_user.username
