from django.shortcuts import render

from catalog.models import Product


def index(request):
    object_list = Product.objects.all()
    context = {
        'object_list': object_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context= {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)

