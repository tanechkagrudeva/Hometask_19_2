from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='previews/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    price = models.DecimalField(max_digits=5 , decimal_places=2, ** NULLABLE, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, **NULLABLE, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False, **NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}, {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

class Category(models.Model):
    objects = None
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
         verbose_name = 'Категория'
         verbose_name_plural = 'Категории'
         ordering = ('name',)


class Record(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='articles/', verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0,verbose_name='Просмотры' )

