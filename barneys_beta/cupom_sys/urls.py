from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_index),
    path('create/', views.post_create),
    path('<int:t_id>', views.post_detail),
    #path('update/', views.post_update),
    #path('delete/', views.post_delete),
]