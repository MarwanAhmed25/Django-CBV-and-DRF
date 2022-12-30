from django.urls import path
from . import views
app_name = 'Model'

urlpatterns = [
    path('', views.Model_ListView.as_view(), name='Models_list'),
    path('update/<str:slug>', views.Model_UpdateView.as_view(), name='Model_update'),
    path('create', views.Model_CreateView.as_view(), name='Model_create'),
    path('delete/<str:slug>', views.Model_DeleteView.as_view(), name='Model_delete'),
    path('<str:slug>', views.Model_DetailView.as_view(), name='Model_detail'),

]