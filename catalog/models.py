from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    category = models.CharField(max_length=75, verbose_name='категория')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category} - {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    title = models.CharField(max_length=75, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/',verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена за штуку')
    date = models.DateField(verbose_name='дата создания')
    fix_date = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


