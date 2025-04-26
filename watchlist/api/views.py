from rest_framework import generics
from .permissions import  ReviewUserOrReadOnly
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from watchlist.models import StreamPlatform, Movie, Review
from .serializers import StreamPlatformSerializer, MovieListSerializer, ReviewSerializer


class StreamPlatformView(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    # permission_classes = [IsAuthenticated]


class StreamPlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [ReviewUserOrReadOnly]
    


class MovieListView(generics.ListCreateAPIView):
    # queryset = WatchList.objects.all()
    serializer_class = MovieListSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Movie.objects.filter(platform=pk)


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = [ReviewUserOrReadOnly]


class ReviewListCreateView(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movie=pk)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [ReviewUserOrReadOnly]
    permission_classes = [IsAuthenticated]




