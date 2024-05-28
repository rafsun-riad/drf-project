from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(),
         name='stream-detail'),
    # path('review', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail')
    path('<int:pk>/review-create/',
         views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/',
         views.ReviewDetail.as_view(), name='review-detail'),
    path('reviews/<str:username>/', views.UserReview.as_view(),
         name='user-review-detail'),

]
