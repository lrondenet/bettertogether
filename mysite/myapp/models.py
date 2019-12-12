from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver

# White board
class WhiteBoard(models.Model):
    subject = models.CharField(max_length=30)
    user = models.ManyToManyField(User)
    whiteboard_key = models.IntegerField()

    def __str__(self):
        return self.subject

class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    image = models.ImageField(blank=True)
    bio = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.first_name


#@receiver(post_save,sender=User)
#def create_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save,sender=User)
#def save_profile(sender, instance, **kwargs):
    #instance.Profile.save()

# create a User profile whenever we created a user
#def create_profile(sender, **kwargs):
#   if kwargs['created']:
#        Profiles = Profile.objects.created(first_name=kwargs['instance'])

#post_save.connect(create_profile, sender=User)        

