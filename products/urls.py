from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
        path('upload-product/', views.upload_product, name='upload_product'),
        path('view-products/', views.view_products, name='view_products'),
        path('product/<int:product_id>/', views.product_details, name='product_details'),
]