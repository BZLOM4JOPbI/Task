# Generated by Django 4.2 on 2023-04-13 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_products_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Товары'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='name_of_product',
            new_name='title_of_product',
        ),
    ]
