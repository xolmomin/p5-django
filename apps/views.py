from django.contrib.admin import ModelAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.templatetags.log import AdminLogNode
from django.db.models import Q, Subquery
from django.http import HttpResponse
from apps.models import Region, District


def index(request):
    regions = Region.objects.all()
    LogEntry.objects.all()
    District.objects.filter(user_id__in=Subquery(Region.objects.values('id')))
    District.objects.filter(region__name='Toshkent shahar')
    return HttpResponse('Hello, world')

# gte, gt, lt, lte
# >=,  > ,  <, <=

'''

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