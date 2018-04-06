from django.urls import path

from . import views

app_name = 'WebAPI'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<order_by>/', views.ordered_view, name='ordered'),
    path('type/<product_type>/', views.producttype_view, name='type'),
]