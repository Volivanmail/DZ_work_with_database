from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort_catalog = request.GET.get('sort')
    catalog = Phone.objects.all()
    if sort_catalog == 'min_price':
        catalog = catalog.order_by('price')
    elif sort_catalog == 'max_price':
        catalog = catalog.order_by('-price')
    elif sort_catalog == 'name':
        catalog = catalog.order_by('name')
    context = {
        'phones': catalog,
               }
    return render(request, template, context=context)



def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug__contains=slug)
    for phone in phones:
        context = {'phone': phone}
    return render(request, template, context)
