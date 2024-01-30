from django.db import models
from django.urls import reverse
from account_module.models import User


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='Title')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='Title in URL')
    is_active = models.BooleanField(verbose_name='active / Deactive')
    is_delete = models.BooleanField(verbose_name='removed / unremoved')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='Brand name', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='Name in URL', db_index=True)
    is_active = models.BooleanField(verbose_name='active / Deactive')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='Product name')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='categories')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='Product image')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='Brand', null=True, blank=True)
    price = models.IntegerField(verbose_name='Price')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='short Description')
    description = models.TextField(verbose_name='main Description', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True, verbose_name='Title in URL')
    is_active = models.BooleanField(default=False, verbose_name='active / Deactive')
    is_delete = models.BooleanField(verbose_name='Removed / Unremoved')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='Title')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'Products Tag'
        verbose_name_plural = 'Products Tags'

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product')
    ip = models.CharField(max_length=30, verbose_name='User IP')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'Products review'
        verbose_name_plural = 'Products Reviews'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='Image')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Gallery image'
        verbose_name_plural = 'Images Gallery'
