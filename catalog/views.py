from django.shortcuts import render
from catalog.models import Product


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}\n{email}\n{message}')

    contex = {
        'title': "Контакты",

    }


    return render(request, 'catalog/contact.html', contex)


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'

    }

    return render(request, 'catalog/product.html', context)

