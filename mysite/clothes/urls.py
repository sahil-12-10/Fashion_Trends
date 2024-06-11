from django.urls import path
from clothes import views

app_name = 'clothes'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('products/',views.products, name='products'),
]