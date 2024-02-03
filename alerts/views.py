from django.core.cache import cache
from django.conf import settings
from rest_framework import generics, permissions
from .models import Alert
from .serializers import AlertSerializer

class AlertCreateView(generics.CreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlertDeleteView(generics.DestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlertListView(generics.ListAPIView):
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        queryset = Alert.objects.filter(user=self.request.user)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def list(self, request, *args, **kwargs):
        # Check if the result is already in the cache
        cache_key = f'alert_list_{request.user.id}_{request.query_params.get("status", "all")}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return self.get_paginated_response(cached_data)

        response = super().list(request, *args, **kwargs)

        # Cache the result
        cache.set(cache_key, response.data, settings.CACHE_TIMEOUT)

        return response