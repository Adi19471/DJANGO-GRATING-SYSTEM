from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver 

# Create your models here.


class update(models.Model):
    image = models.ImageField(upload_to="Profile_pics",default='user.png')
    age = models.IntegerField(default=18)

    p = models.OneToOneField(User,on_delete=models.CASCADE)


@receiver(post_save,sender=User)

def createprofile(sender,instance,created,**kwargs):
    if created:
        update.objects.create(p=instance)