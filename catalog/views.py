from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Record


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/index.html'


class RecordCreateView(CreateView):
    model = Record
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)


class RecordUpdateView(UpdateView):
    model = Record
    fields = ('title', 'content',)

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_record', args=[self.kwargs.get('pk')])


class RecordListView(ListView):
    model = Record

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


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
