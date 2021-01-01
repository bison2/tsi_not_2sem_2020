from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class HomeView(TemplateView):    
    template_name = 'pay/homepay.html'
    def get_context_data(self, **kwargs): # new         
        context =super().get_context_data(**kwargs)        
        context['key'] = settings.PUBLISHABLE_KEY        
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 1000,
            currency='usd',
            description='teste pagamento',
            source=request.POST['stripeToken']
        )
        context = {
                'title':'Página de pagamento',
                'content':'pagamento realizado com sucesso!'
        }
        return render(request, 'charge.html', context)