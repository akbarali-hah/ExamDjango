from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView, UpdateView, DeleteView, CreateView

from apps.forms import ProductForm, RegisterForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import Product


# Create your views here.
class IndexView(TemplateView):
    template_name = 'apps/home.html'


class RegisterFormView(FormView):
    template_name = 'apps/profile/login.html'
    form_class = RegisterForm
    success_url = reverse_lazy('register_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(NotLoginRequiredMixin, LoginView):
    next_page = 'index_page'
    template_name = 'apps/profile/login.html'


class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.order_by('-created_at')
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'


class CreateUpdateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'apps/product/product_add.html'
    success_url = reverse_lazy('product_list_page')


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'apps/product/product_update.html'
    success_url = reverse_lazy('product_list_page')


class DeleteProductView(DeleteView):
    model = Product
    pk_url_kwarg = 'pk'
    form = ProductForm
    template_name = 'apps/product/product-list.html'
    success_url = reverse_lazy('product_list_page')

    def get(self, request, pk):
        Product.objects.filter(id=pk).delete()
        return redirect('product_list_page')
