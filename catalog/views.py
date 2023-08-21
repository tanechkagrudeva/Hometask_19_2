from django.forms import modelformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm

from catalog.models import Product, Record, Version


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        active_versions = Version.objects.filter(is_current_version=True).select_related('product')
        active_products = {version.product_id: version for version in active_versions}
        for product in queryset:
            product.active_version = active_products.get(product.id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['products'] = queryset
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/index.html'



class ProductCreateView(CreateView):
    model = Record
    #fields = ('title', 'content',)
    #form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_formset = modelformset_factory(Product, form=ProductForm, extra=1)
        context_data['title'] = 'Добавить товар'
        if self.request.method == 'POST':
            context_data['formset'] = product_formset(self.request.POST)
        else:
            context_data['formset'] = product_formset()
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Record
    fields = ('title', 'content',)
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_formset = modelformset_factory(Product, form=ProductForm, extra=1)
        context_data['title'] = 'Редактировать товар'
        if self.request.method == 'POST':
            context_data['formset'] = product_formset(self.request.POST)
        else:
            context_data['formset'] = product_formset()
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            new_id = form.save()
            new_id.slug = slugify(new_id.title)
            new_id.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_record', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')


class RecordListView(ListView):
    model = Record

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class RecordCreateView(CreateView):
    model = Record
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:records')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)

class RecordUpdateView(UpdateView):
    model = Record
    fields = ('title', 'content',)
    # success_url = reverse_lazy('catalog:records')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_record', args=[self.kwargs.get('pk')])


class RecordDetailedView(DetailView):
    model = Record


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('catalog:list')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}\n{email}\n{message}')

    contex = {
        'title': "Контакты",

    }

    return render(request, 'catalog/contact.html', contex)
