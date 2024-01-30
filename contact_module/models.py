from django.db import models


# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    email = models.EmailField(max_length=300, verbose_name='Email')
    full_name = models.CharField(max_length=300, verbose_name='Name And Family Name')
    message = models.TextField(verbose_name='Contact us Content')
    created_date = models.DateTimeField(verbose_name='Submit Date', auto_now_add=True)
    response = models.TextField(verbose_name='Answers Date', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='Read by Admin', default=False)

    class Meta:
        verbose_name = 'contact us'
        verbose_name_plural = 'contact us list'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')
