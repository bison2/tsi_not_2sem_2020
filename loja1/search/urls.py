from django.urls import path

app_name = "search"

from .views import (
           # ProductListView, 
            SearchProductView,        )
urlpatterns = [
    path('', SearchProductView.as_view(), name='list'),
]