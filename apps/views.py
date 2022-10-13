from http import HTTPStatus
from random import random, choices, randint, choice

from django.contrib.admin import ModelAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.templatetags.log import AdminLogNode
from django.db.models import Q, Subquery, F
from django.http import HttpResponse
from django.shortcuts import render

from apps.models import Region, District, Product, Category


def index_page(request):
    return render(request, 'apps/index.html')


def about_page(request):
    return render(request, 'apps/about.html')


# gte, gt, lt, lte
# >=,  > ,  <, <=

'''
    # regions = Region.objects.all()
    # for region in regions:
    #     region.delete()


    # category = Category.objects.first()
    # category.product_set.all()
    # category.id
    # category.pk

    # Category.objects.bulk_create([
    #     Category(name='Bolalar dunyosi'),
    #     Category(name='Transport'),
    #     Category(name='Hayvonlar'),
    #     Category(name="Ko'chmas mulk"),
    #     Category(name='Ish')
    # ])

    # categories = Category.objects.values_list('id', flat=True)
    # products = []
    # for i in range(1000, 1000_000):
    #     products.append(
    #         Product(**{
    #             'name': f'Product {i}',
    #             'slug': f'product-{i}',
    #             'price': randint(1, 100) * 100,
    #             'description': f'Description {i}',
    #             # 'category': Category.objects.first(),
    #             'category_id': choice(categories)
    #         })
    #     )
    #
    # Product.objects.bulk_create(products, 1000)

    # Product 1-100
    # 1000-100000
    # Description 1-100
    # category 1-3

    # regions = Region.objects.all()
    # LogEntry.objects.all()
    # District.objects.filter(region_id__in=Subquery(Region.objects.values('id')))
    # District.objects.filter(region__name='Toshkent shahar')
    # districts = District.objects.all()[1:4]
    # Product.objects.all()[:50].annotate(chegirma=F())
    # print(123)

pbkdf2_sha256$390000$CTdar3wsHWQCiZAgTBOGKm$2QJwVMNd6bgkbeUvEH02ddRtbpphIaXk/fRuuIhZg40=
pbkdf2_sha256$390000$AIUaT4ZhXbXbeYNWEPJYqe$nvnPTN3irdAd68TgDmmU/agMNbLzerOuA7YenmlChqw=


Django ORM

1) filter(<condition_1>, <condition_2>)
2) queryset_1 & queryset_2
3) filter(Q(<condition_1>) & Q(<condition_2>))

1) Region.objects.filter(name__startswith='T', name__endswith='viloyati')
2) Region.objects.filter(name__startswith='T') & Region.objects.filter(name__endswith='viloyati')
3) Region.objects.filter(Q(name__startswith='T') & Q(name__endswith='viloyati'))


1) Region.objects.exclude(name__startswith='T')
2) Region.objects.filter(~Q(name__startswith='T'))


Region.objects.filter(~Q(id__lt=5))    not id < 5
Region.objects.filter(id__gte=5)


q1 = Region.objects.filter(id__gte=5)  5-14
q2 = Region.objects.filter(id__lt=12)  1-11


Region.objects.all()


Category
Product
Cart
Wishlist

'''
