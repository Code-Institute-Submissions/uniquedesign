# Generated by Django 2.2.13 on 2020-09-01 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Papermake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Papertype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Quantity',
            },
        ),
        migrations.CreateModel(
            name='Thicknes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(default='Name', max_length=254)),
                ('company', models.CharField(default='Company Name', max_length=254)),
                ('address', models.CharField(default='Company Address', max_length=254)),
                ('tel', models.DecimalField(decimal_places=0, default='1234', max_digits=8)),
                ('email', models.EmailField(default='eMail Address', max_length=254)),
                ('price', models.DecimalField(decimal_places=2, default='200', max_digits=6)),
                ('footer', models.BooleanField(blank=True, default=False, null=True)),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('info', models.CharField(default='Registration Information', max_length=254)),
                ('cardtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='design.Cardtype')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='design.Category')),
                ('edge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='design.Edge')),
                ('make', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='design.Papermake')),
                ('paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='design.Papertype')),
                ('quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='design.Quantity')),
                ('thicknes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='design.Thicknes')),
            ],
        ),
    ]
