from django.db import models


class Products(models.Model):
    
    # brand_name = models.CharField('Бренд', max_length=50)
    title_of_product = models.CharField('Название товара', max_length=50)
    type_of_product = models.CharField('Тип продукта', max_length=50)
    # description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена')

    class Meta:

        verbose_name_plural = 'Товары'


    def __str__(self):
        return f'(ID: {self.id})    {self.title_of_product}'