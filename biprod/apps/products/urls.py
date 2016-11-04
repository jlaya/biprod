from django.conf.urls import url
from .views import ProductsCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = (
               url(r'^products$', ProductsCreateView.as_view(), name='products'),
              )
