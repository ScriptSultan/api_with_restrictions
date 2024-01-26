from django_filters import rest_framework as filters, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    published = DateFromToRangeFilter()
    class Meta:
        model = Advertisement
        fields = ['published', 'status']