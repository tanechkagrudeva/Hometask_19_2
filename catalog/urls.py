from django.urls import path


from catalog.apps import MainConfig
from catalog.views import contact, ProductListView, ProductDetailView, RecordListView, RecordCreateView, \
    RecordDetailedView, RecordUpdateView, RecordDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('product/', ProductDetailView.as_view(), name='product'),
    path('', RecordListView.as_view(), name='articles'),
    path('create/', RecordCreateView.as_view(), name='create_record'),
    path('view/<int:pk>/', RecordDetailedView.as_view(), name='view_record'),
    path('edit/<int:pk>/', RecordUpdateView.as_view(), name='edit_record'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete_record'),
]

