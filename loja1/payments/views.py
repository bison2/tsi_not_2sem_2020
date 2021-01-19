from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe
from carts.models import Cart, m2m_changed_cart_receiver
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, JsonResponse, request 

stripe.api_key = settings.STRIPE_SECRET_KEY

def valor_total(request,pk):
    usuario = request.user
    total = Cart.objects.all().filter(id=pk).values_list('total', flat=True)
    return total[0]

class HomeView(TemplateView):    
    template_name = 'pay/homepay.html'
    
    def get_context_data(self, **kwargs): # new         
        context =super().get_context_data(**kwargs)        
        context['key'] = settings.PUBLISHABLE_KEY 
        context['total'] = valor_total(self.request, self.kwargs['pk'])       
        context['total2'] = 100*valor_total(self.request, self.kwargs['pk'])       
        context['id'] = self.kwargs['pk']
        return context

#success url--> charge
def charge(request, pk):
    amt = 100*valor_total(request, pk)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = int(amt),
            currency='usd',
            description='teste pagamento',
            source=request.POST['stripeToken']
        )
        context = {
                'title':'Página de pagamento',
                'content':'pagamento realizado com sucesso!'
        }
        return render(request, 'charge.html', context)