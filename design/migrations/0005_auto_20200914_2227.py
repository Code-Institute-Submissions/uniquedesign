# Generated by Django 2.2.13 on 2020-09-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_quantity_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='name',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thicknes',
            name='name',
            field=models.IntegerField(),
        ),
    ]