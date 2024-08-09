
from django.urls import path
from .views import *

urlpatterns = [
    path('StudentList/',StudentList.as_view(),name='stu_list'),
    path('stu_info/<int:pk>',StudentDetail.as_view(),name='stu_details'),
    # path('list/',list,name='list')
]

