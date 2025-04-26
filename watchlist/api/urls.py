from django . urls import path
from .views import (StreamPlatformView, StreamPlatformDetailView, MovieListView,
                     MovieDetailView, ReviewListCreateView , ReviewDetailView)


urlpatterns = [
    path("stream-platform/", StreamPlatformView.as_view(), name="streamplatform-list"),
    path("stream-platform/<int:pk>/", StreamPlatformDetailView.as_view(), name="streamplatform-detail"),

    path("movie/<int:pk>/platform/", MovieListView.as_view(), name="movie-list"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movielist-detail"),

    path("movie/<int:pk>/review/", ReviewListCreateView.as_view(), name="review-list"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
    
]
