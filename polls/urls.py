from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sec/', views.MyProtectedEndPoint.as_view(), name='index'),
    re_path(r'^subjects/$',
views.SubjectListView.as_view(),
name='subject_list'),
# re_path(r'^subjects/(?P<pk>\d+)/$',
# views.SubjectDetailView.as_view(),
# name='subject_detail'),
path('subjects/<pk>/', views.SubjectDetailView.as_view()),
]