from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAutherOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [AdvertisementFilter]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAutherOrReadOnly]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
