from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='dashboard_with_plot'),
    path('data', views.pivot_data, name='plot_data'),
]