from django.db import models
from jalali_date import date2jalali
from account_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.CASCADE, verbose_name='main category')
    title = models.CharField(max_length=200, verbose_name='category title')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='title in URL')
    is_active = models.BooleanField(default=True, verbose_name='active / deactive')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Articles Category'


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='Article title')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='title in URL')
    image = models.ImageField(upload_to='images/articles', verbose_name='Article image')
    short_description = models.TextField(verbose_name='short description')
    text = models.TextField(verbose_name='Article content')
    is_active = models.BooleanField(default=True, verbose_name='Active / Deactive')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='categories')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Writer', null=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Register Date')

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article')
    parent = models.ForeignKey('ArticleComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='parent')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Register Date')
    text = models.TextField(verbose_name='comment content')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Article comment'
        verbose_name_plural = 'Articles Comments'
