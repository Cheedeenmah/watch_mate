from rest_framework.pagination import PageNumberPagination

class StreamPlatformPagination(PageNumberPagination):
    page_size = 3