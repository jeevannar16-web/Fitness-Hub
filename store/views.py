from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    category = request.GET.get('category')

    if category:
        products = products.filter(category__name=category)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=product.category).exclude(pk=pk)[:3]
    context = {
        'product': product,
        'related': related,
    }
    return render(request, 'store/product_detail.html', context)
