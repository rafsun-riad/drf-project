from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', views.StreamPlatformDetailAV.as_view(),
         name='stream-detail')
]
