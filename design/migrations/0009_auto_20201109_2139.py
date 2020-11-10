# Generated by Django 2.2.13 on 2020-11-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0008_auto_20200918_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='category',
            field=models.CharField(default=100, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thicknes',
            name='category',
            field=models.CharField(default=100, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='thicknes',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
