from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.formfields import PhoneNumberField 
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):

    def create_user(self,email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if password is None:
            raise TypeError('Users must have a password.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,  email, password, **kwargs):
     
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(default=timezone.now)
   
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
 

    USERNAME_FIELD = 'email'


    objects = UserManager()
    
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        fullname = "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)
        return fullname

    def email_user(self, subject, message, from_email=None):
      
    
        send_mail(subject, message, from_email, [self.email])

    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
class Profile(models.Model):
    user=models.OneToOneField('User',on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="uploads", blank=False, null=False,default='default.png')
    user_bio = models.CharField(max_length=600, blank=True)
    premium=models.BooleanField(default=False)
    
    def get_user_full_name(self):
        return self.user.get_full_name()
    
    

    
    


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()