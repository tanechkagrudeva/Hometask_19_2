from django.urls import path
from django.conf.urls.static import static


from catalog.views import index, contact, product

urlpatterns = [
    path('', index),
    path('contacts/', contact),
    path('product/', product),
]

