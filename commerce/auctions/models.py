from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class NewListings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    bid = models.IntegerField()
    image = models.URLField(default='https://tazacommune.com/wp-content/plugins/wp-appkit/default-themes/q-ios/img/img-icon.svg', null=True)
    category = models.CharField(max_length=64)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.title}, starting at {self.bid}"