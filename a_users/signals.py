from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    # add profile if user created
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            
            email_address = EmailAddress.objects.get_primary(instance)
            if email_address.email != instance.email:
                email_address.email = instance.email
                email_address.verified = False
                email_address.save()
        except:
            # if all auth email address does not exist
            EmailAddress.objects.create(user=instance, email=instance.email, primary=True, verified=False)

@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    # delete profile if user deleted
    if instance.username:
        instance.username = instance.username.lower()
        

@receiver(post_save, sender=Profile)
def update_coount_email(sender, instance, created, **kwargs):
    # add email address if profile created
    try:
        if created:
            email_address = EmailAddress.objects.get_primary(instance.user)
            if email_address and email_address.email != instance.user.email:
                email_address.email = instance.user.email
                email_address.verified = False
                email_address.save()
    except Exception as e:
        print(f"Somethin went wrong in update_coount_email | Error: {e}")