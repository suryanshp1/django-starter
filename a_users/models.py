from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    displayname = models.CharField(max_length=100, blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        return self.displayname or self.user.username

    @property
    def avatar(self):
        try:
            avatar = self.avatar.url
        except:
            avatar = static('images/avatar.svg')
        return avatar