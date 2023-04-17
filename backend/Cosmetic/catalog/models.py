from django.db import models


class Creams(models.Model):
    
    # Информационные поля
    brand = models.CharField('Бренд', max_length=50)

    title_of_product = models.CharField(
                                        'Название товара', 
                                        max_length=50, 
                                        blank=True,
                                        )

    brief_info_about_product = models.CharField(
                                                'Краткое описание', 
                                                max_length=25, 
                                                blank=True,
                                                )

    description = models.TextField('Описание', blank=True)

    price = models.PositiveIntegerField('Цена')
    

    # Поля для фильтрации тораров
    cream_for = models.CharField('Крем для', max_length=20)
    
    type_of_derm = models.CharField('Тип кожи', max_length=50)

    class Meta:

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return f'(ID: {self.id}) brand: {self.brand} name: {self.title_of_product}'