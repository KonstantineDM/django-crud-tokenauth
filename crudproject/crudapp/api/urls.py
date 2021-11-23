from crudapp.api import views
from django.urls import path


app_name = 'crudapp'
urlpatterns = [
    path('create', views.AccountViewset.as_view({'post': 'create'}), name='create'),
    path('<int:pk>', views.AccountViewset.as_view({'get': 'retrieve'}), name='read'),
    path('accounts/', views.AccountViewset.as_view({'get': 'list'}), name='read_all'),
    path('<int:pk>/update', views.AccountViewset.as_view({'put': 'update'}), name='update'),
    path('<int:pk>/delete', views.AccountViewset.as_view({'delete': 'destroy'}), name='delete'),
]
