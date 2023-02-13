from . import views
from django.urls import path
app_name='shopapp'

urlpatterns = [

    path('',views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/',views.allproductcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productdetail,name='productcatdetail'),
]
