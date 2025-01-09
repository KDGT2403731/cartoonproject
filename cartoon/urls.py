from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('cartoon/', views.ListCartoonView.as_view(), name='list-cartoon'),
    path('cartoon/<int:pk>/detail/', views.DetailCartoonView.as_view(), name='detail-cartoon'),
    path('cartoon/create/', views.CreateCartoonView.as_view(), name='create-cartoon'),
    path('cartoon/<int:pk>/update/', views.UpdateCartoonView.as_view(), name='update-cartoon'),
    path('cartoon/<int:cartoon_id>/review/', views.CreateReview.as_view(), name='review'),
]