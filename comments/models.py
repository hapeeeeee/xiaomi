from django.db import models
from django.contrib.auth import get_user_model
from xmsc.models import Phone
from django.utils.timezone import now

# Create your models here.

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="评论用户", on_delete=None, null=True)
    phone = models.ForeignKey(Phone, verbose_name="手机型号", on_delete=None, null=True)
    content = models.CharField(max_length=200, verbose_name="内容")
    time = models.DateTimeField(default=now(), verbose_name="评论时间")

    def __str__(self):
        return "{} 评论了 {} 手机型号{} 时间{}".format(self.user, self.content, self.phone, self.time)

    class Meta:
        verbose_name = "手机评论"
        verbose_name_plural = verbose_name
