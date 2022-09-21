from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('apply-list',views.applyList,name='apply-list'),
    path('apply-detail/<str:pk>',views.applyDetail,name='apply-detail'),
    path('apply-create',views.applyCreate,name='apply-create'),
    path('apply-delete/<str:pk>',views.applyDelete,name='apply-delete'),
    path('apply-update/<str:pk>',views.applyUpdate,name='apply-update'),
    ]