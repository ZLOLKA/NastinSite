from django.shortcuts import render
from Home.models import Category, Product


# Create your views here.
def home_view(request):
    products = Product.objects.all()[:3]
    categories = Category.objects.all()[:]
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'Home.html', context)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, "Product.html", context)


def test(request):
    return render(request, 'test.html')
