# Generated by Django 3.1.6 on 2021-02-22 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['ordering'], 'verbose_name_plural': 'Categories'},
        ),
    ]
