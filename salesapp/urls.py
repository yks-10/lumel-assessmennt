from django.urls import path
from salesapp import views


urlpatterns = [
    path('', views.HealthView.as_view(), name="Health-Check"),
    path('customer', views.CustomerView.as_view(), name="customer"),
    path('order', views.OrderView.as_view(), name="order"),
    path('product', views.ProductView.as_view(), name="product"),
    path('data', views.DataImport.as_view(), name="data"),
]