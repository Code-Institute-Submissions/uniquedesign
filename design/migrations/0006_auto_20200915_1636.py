# Generated by Django 2.2.13 on 2020-09-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0005_auto_20200914_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='friendly_name',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thicknes',
            name='friendly_name',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=6),
            preserve_default=False,
        ),
    ]