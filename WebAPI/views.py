from django.views import generic
from .models import Product
from django.shortcuts import render
from django.db.models import F


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'WebAPI/ordered.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        """Returns all products."""
        return Product.objects.all()


def ordered_view(request, order_by):
    product_list = Product.objects
    if order_by == 'discount':
        for product in product_list.all():
            p = product_list.get(name=product.name)
            p.discount = F('price') - F('custom_label_0')
            p.save()
    elif order_by == 'discounted':
        order_by = '-custom_label_0'

    product_list = Product.objects.order_by(order_by)[:20]
    context = {'product_list': product_list}
    return render(request, 'WebAPI/ordered.html', context)


def producttype_view(request, product_type):
    product_list = Product.objects.filter(type=product_type).order_by('price')
    context = {'product_list': product_list}
    return render(request, 'WebAPI/ordered.html', context)