from crudapp.api import views
from django.urls import path


app_name = 'crudapp'
urlpatterns = [
    path('create', views.api_account_create, name='create'),
    path('<int:acc_id>', views.api_account_read, name='read'),
    path('accounts/', views.api_account_read_all, name='read_all'),
    path('<int:acc_id>/update', views.api_account_update, name='update'),
    path('<int:acc_id>/delete', views.api_account_delete, name='delete'),
]
