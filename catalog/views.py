from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class AdminWriteReadOnlyPublicMixin:
    def get_permissions(self):
        if self.request.method in ("GET", "HEAD", "OPTIONS"):
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class CategoryViewSet(AdminWriteReadOnlyPublicMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(AdminWriteReadOnlyPublicMixin, viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").filter(is_active=True)
    serializer_class = ProductSerializer
