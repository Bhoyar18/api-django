# usingmixins api
from django.urls import path
from mixinapi import views

urlpatterns=[
    path('snippets/',views.SnippetList.as_view()),
    path('snippets/<int:pk>/',views.SnippetDetail.as_view()),

]