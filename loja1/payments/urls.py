from django.urls import path
from . import views
urlpatterns = [ 
    path('charge/', views.charge, name='charge'),   
    path('', views.HomeView.as_view(), name='homepay'),
]