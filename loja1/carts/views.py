from django.shortcuts import render
from .models import Cart 




def cart_home(request):
    #cart_obj = Cart.objects.new_or_get(request) 
    queryset = Cart.objects.all()
    

    #list_cart = Cart.objects.pedido()
    context = {
            'objects': queryset,
            
     #       'list_cart': list_cart
    }
    return render(request, "carts/home.html", context)
    


