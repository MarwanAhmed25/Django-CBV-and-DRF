from django.urls import path
from . import views
app_name = 'Types'

urlpatterns = [
    path('', views.TypeListView.as_view(), name='Types_list'),
    path('update/<str:slug>', views.TypeUpdateView.as_view(), name='Type_update'),
    path('create', views.TypeCreateView.as_view(), name='Type_create'),
    path('delete/<str:slug>', views.TypeDeleteView.as_view(), name='Type_delete'),
    path('<str:slug>', views.TypeDetailView.as_view(), name='Type_detail'),

]