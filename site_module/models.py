from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='Website Name')
    site_url = models.CharField(max_length=200, verbose_name='Website Domain')
    address = models.CharField(max_length=200, verbose_name='Address')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='Phone number')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='Fax')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email')
    copy_right = models.TextField(verbose_name='Copy right content')
    about_us_text = models.TextField(verbose_name='About Us Content')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='Website Logo')
    is_main_setting = models.BooleanField(verbose_name='Main Setting')

    class Meta:
        verbose_name = 'Website Setting'
        verbose_name_plural = 'Setting'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')

    class Meta:
        verbose_name = 'Footers Links Category'
        verbose_name_plural = 'Footers Links Categories'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    url = models.URLField(max_length=500, verbose_name='Link')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        verbose_name = 'Footers Link'
        verbose_name_plural = 'Footers Links'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    url = models.URLField(max_length=500, verbose_name='Link')
    url_title = models.CharField(max_length=200, verbose_name='Link Title')
    description = models.TextField(verbose_name='Slider Description')
    image = models.ImageField(upload_to='images/sliders', verbose_name='Sliders image')
    is_active = models.BooleanField(default=True, verbose_name='active / Deactive')

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list = 'product_list', 'Products List Page',
        product_detail = 'product_detail', 'Products Detail Page',
        about_us = 'about_us', 'About Us'

    title = models.CharField(max_length=200, verbose_name='Baner Title')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='Banner Address')
    image = models.ImageField(upload_to='images/banners', verbose_name='Banner Image')
    is_active = models.BooleanField(verbose_name='active / De active')
    position = models.CharField(max_length=200, choices=SiteBannerPositions.choices, verbose_name='Show Place')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Advertising Banner'
        verbose_name_plural = 'Advertising Banners'
