from django.urls import path
from . import views
urlpatterns = [
    path("product_detail/",views.product_html,name = 'product_html')
]