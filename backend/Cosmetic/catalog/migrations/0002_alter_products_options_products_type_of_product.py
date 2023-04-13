# Generated by Django 4.2 on 2023-04-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Товары', 'verbose_name_plural': 'Товар'},
        ),
        migrations.AddField(
            model_name='products',
            name='type_of_product',
            field=models.CharField(default='', max_length=50, verbose_name='Тип продукта'),
            preserve_default=False,
        ),
    ]
