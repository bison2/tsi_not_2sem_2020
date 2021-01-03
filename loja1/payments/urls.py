from django.urls import path
from . import views


urlpatterns = [ 
    path('charge/<int:pk>/', views.charge, name='charge'),   
    path('<int:pk>/', views.HomeView.as_view(), name='homepay'),
]