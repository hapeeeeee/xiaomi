from django.db import models
from uuid import uuid4

# Create your models here.

def upload_image(instance, filename):
    image_end = filename.split('.')

    res_filename = uuid4().hex

    return "phone/{}.{}".format(res_filename, image_end[-1])


class Category(models.Model):
    name = models.CharField(max_length=50,)

    class Meta:
        verbose_name = "手机分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to=upload_image, blank=True)
    small_img = models.ImageField(upload_to=upload_image, blank=True)
    kind = models.ForeignKey(Category, verbose_name="分类", on_delete=None, default=None, null=True)

    class Meta:
        verbose_name = "手机"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name