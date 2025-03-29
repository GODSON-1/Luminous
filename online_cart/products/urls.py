
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import list_products, mens_products,detail_product, womens_products, accessories_products  # noqa: F401


urlpatterns = [
    path("", views.index,name='home'),
    path('blog/', views.blog_page, name='blog_page'),
    path("product_list", views.list_products,name='list_product'),
    path('product_list/men/', views.mens_products, name='mens_products'),
    path('product_list/women/', views.womens_products, name='womens_products'),
    path('product_list/accessories/', views.accessories_products, name='accessories_products'),
    path("product_detail/<pk>",views.detail_product,name='detail_product'),
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)