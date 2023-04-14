from django.db import models


class Creams(models.Model):
    
    brand = models.CharField('Бренд', max_length=50)

    title_of_product = models.CharField('Название товара', max_length=50)

    type_of_derm = models.CharField('Тип кожи', max_length=50)

    description = models.TextField('Описание', null=True)

    price = models.PositiveIntegerField('Цена')
    
    cream_for = models.CharField('Крем для', max_length=20)
    

    class Meta:

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return f'(ID: {self.id}) {self.title_of_product}'