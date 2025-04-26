from django.contrib import admin

from .models import StreamPlatform, Movie, Review
# Register your models here.


admin.site.register(StreamPlatform)
admin.site.register(Movie)
admin.site.register(Review)

