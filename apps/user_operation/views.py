from rest_framework import viewsets, mixins

from .models import UserFav
from .serializers import UserFavSerializer


class UserFavViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.ListModelMixin):
    """
    用户收藏功能
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
