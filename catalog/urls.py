from django.urls import path


from catalog.apps import MainConfig
from catalog.views import index, contact, product

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
]

