from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='notice_home' ),
    path('api/notice', views.notice_collection, name='notice_collection'),
    path('api/notice/<int:pk>', views.notice_element, name='notice_element'),
    path('api/notice/create', views.notice_element_create, name='notice_element_create')
]
