from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Cardtype(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_price(self):
        return self.price


class Edge(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_price(self):
        return self.price


class Header(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Papermake(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_price(self):
        return self.price


class Papertype(models.Model):
    name = models.CharField(max_length=254, default='na')
    friendly_name = models.CharField(max_length=254, default='NA')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_price(self):
        return self.price


class Quantity(models.Model):

    class Meta:
        verbose_name_plural = 'Quantity'

    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    friendly_name = models.DecimalField(max_digits=6, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name

    def get_category(self):
        return self.category

    def get_friendly_name(self):
        return self.friendly_name

    def get_price(self):
        return self.price


class Thicknes(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    friendly_name = models.DecimalField(max_digits=6, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name

    def get_category(self):
        return self.category

    def get_friendly_name(self):
        return self.friendly_name

    def get_price(self):
        return self.price


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, default='Name')
    company = models.CharField(max_length=254, default='Company Name')
    address = models.CharField(max_length=254, default='Company Address')
    tel = models.DecimalField(max_digits=8, decimal_places=0, default='1234')
    email = models.EmailField(max_length=254, default='eMail Address')
    price = models.DecimalField(max_digits=6, decimal_places=0)
    quantity = models.ForeignKey('Quantity', null=True, blank=True, on_delete=models.SET_NULL)
    edge = models.ForeignKey('Edge', null=True, blank=True, on_delete=models.SET_NULL)
    cardtype = models.ForeignKey('Cardtype', null=True, blank=True, on_delete=models.SET_NULL)
    thicknes = models.ForeignKey('Thicknes', null=True, blank=True, on_delete=models.SET_NULL)
    paper = models.ForeignKey('Papertype', null=True, blank=True, on_delete=models.SET_NULL)
    make = models.ForeignKey('Papermake', null=True, blank=True, on_delete=models.SET_NULL)
    header = models.ForeignKey('Header', null=True, blank=True, on_delete=models.SET_NULL)
    footer = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    logo = models.ImageField(upload_to='media/', default='media/noimage.jpg', null=True, blank=True)
    info = models.CharField(max_length=254, default='Description')

    def __str__(self):
        return self.name
