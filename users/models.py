from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import  get_user_model
from xmsc.models import Phone



class Users(AbstractUser):
    gender = models.BooleanField(choices=((True, "男"), (False, "女")),default=True,verbose_name="性别")
    phone = models.CharField(max_length=20)

User = get_user_model()

class GouWuche(models.Model):
    user = models.ForeignKey(User, verbose_name="购买用户")
    phone = models.ForeignKey(Phone, verbose_name="购买商品")

    def __str__(self):
        return "{}准备购买{}".format(self.user.username, self.phone.name)