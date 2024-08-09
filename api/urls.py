from django.urls import path
from .views import *

urlpatterns = [
    path('stu_lists/',stu_list,name='stu_list'),
    path('stu_info/<int:pk>',stu_details,name='stu_details'),
    # path('list/',list,name='list')
]


