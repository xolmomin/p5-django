from django.db.models import (Model, CharField, FloatField, ForeignKey, CASCADE, IntegerField, SlugField, UUIDField)
from django.utils.text import slugify
import uuid


class Region(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name}'


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('Region', CASCADE)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Category(Model):
    name = CharField(max_length=255, null=False)
    slug = SlugField(max_length=255, blank=True, null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Product(Model):
    name = CharField(max_length=255, null=False)
    slug = SlugField(max_length=255, null=False, unique=True)
    price = FloatField(null=False)
    description = CharField(max_length=255)
    category = ForeignKey('Category', CASCADE, null=False)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.category}'


class Cart(Model):
    product = ForeignKey('Product', CASCADE, null=False)
    quantity = IntegerField(default=1)

    def __str__(self):
        return f'{self.id}'


class Wishlist(Model):
    product = ForeignKey('Product', CASCADE)
    user = ForeignKey('auth.User', CASCADE)
