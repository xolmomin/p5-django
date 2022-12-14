from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from apps import forms
from apps.forms import CustomUserCreationForm, LoginForm
from apps.models import Contact
from root.settings import EMAIL_HOST_USER


def index_page(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'apps/index.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    forms = LoginForm()
    context = {
        'forms': forms
    }
    return render(request, 'apps/auth/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login_page')


def send_information_message(email: str):
    token = '432432'
    context = {
        'token': token
    }
    html_content = render_to_string('apps/email/notification.html', context)
    email = EmailMessage('subject', html_content, EMAIL_HOST_USER, [email], )
    email.content_subtype = 'html'
    response = email.send()
    print(response)



def register_page(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            send_information_message(email)
            return redirect('index')

    context = {
        'forms': form
    }
    return render(request, 'apps/auth/register.html', context)


def form_page(request):
    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST, request.FILES)
        contact_form.save()

        return redirect('index_page')

        # contact_form = forms.ContactForm(request.POST)
        # contact_form.is_valid()
        # contact = Contact(**contact_form.cleaned_data)
        # contact.save()
        # print(1)

        # data = request.POST.dict()
        # data.pop('encoding')
        # data.pop('__len__')
        # data.pop('csrfmiddlewaretoken')
        # contact = Contact(**data)
        # contact.save()

        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # phone = request.POST.get('phone')
        # position = request.POST.get('position')
        # address = request.POST.get('address')
        # contact = Contact(
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     phone=phone,
        #     position=position,
        #     address=address
        # )
        # contact.save()

    return render(request, 'apps/form.html')


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
