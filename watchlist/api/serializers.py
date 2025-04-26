from rest_framework import serializers
from watchlist.models import StreamPlatform, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Review
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  

    class Meta:
        model = Movie
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"