from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

#Class Based View
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()
    template_name = "app_produtos/list.html"
    
    #def get_context_data(self):
        #context = super(ProductListView, self).get_context_data(*args, **kwargs)
        #print(context)
        #return context

#Function Based View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "app_produtos/list.html", context)

#Class Based View
class ProductDetailView(DetailView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()
    template_name = "app_produtos/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

#Function Based View
def product_detail_view(request, pk=None, *args, **kwargs):
    #print(args)
    #print(kwargs)
    #instance = Product.objects.get(pk = pk) #get the object id
    instance = get_object_or_404(Product, pk = pk)
    context = {
        'object': instance
    }
    #queryset = Product.objects.all()
    #context = {
     #   'object_list': queryset
    #}
    return render(request, "app_produtos/detail.html", context)