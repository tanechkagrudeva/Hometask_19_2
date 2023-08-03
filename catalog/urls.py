from django.urls import path


from catalog.apps import MainConfig
from catalog.views import contact, ProductListView, ProductDetailView, RecordListView, RecordCreateView, \
    RecordDetailedView, RecordDeleteView, ProductDeleteView, ProductUpdateView,ProductCreateView, RecordUpdateView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='create_product'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('record/', RecordListView.as_view(), name='records'),
    path('create/', RecordCreateView.as_view(), name='create_record'),
    path('view/<int:pk>/', RecordDetailedView.as_view(), name='view_record'),
    path('edit/<int:pk>/', RecordUpdateView.as_view(), name='edit_record'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete_record'),
]



