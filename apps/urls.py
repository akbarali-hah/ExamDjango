from django.contrib.auth.views import LogoutView
from django.urls import include, path

from apps.views import (CreateUpdateView, CustomLoginView, IndexView, ProductsListView, RegisterFormView,
                        UpdateProductView, DeleteProductView)

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('products', ProductsListView.as_view(), name='product_list_page'),
    path('product/add/', CreateUpdateView.as_view(), name='add_product_page'),
    path('product/edit/<int:pk>', UpdateProductView.as_view(), name='update_product_page'),
    path('product/delete/<int:pk>', DeleteProductView.as_view(), name='delete_product_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('logout', LogoutView.as_view(next_page='login_page'), name='logout_page'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]
