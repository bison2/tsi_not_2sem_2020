from django.shortcuts import render
from .models import Cart 

def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request) 
    queryset = Cart.objects.all()
    context = {
            'objects': queryset
    }
    return render(request, "carts/home.html", context)
    