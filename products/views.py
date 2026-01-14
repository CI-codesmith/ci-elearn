import time
from django.conf import settings
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import Product
from .serializers import ProductSerializer


class ProductSearchPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductSearchAPIView(APIView):
    permission_classes = [AllowAny]
    pagination_class = ProductSearchPagination

    def _timer(self) -> float:
        return time.perf_counter()

    @method_decorator(cache_page(60))
    def get(self, request):
        start = self._timer()
        query = (request.query_params.get("q") or "").strip()
        category = (request.query_params.get("category") or "").strip()

        products = Product.objects.select_related("category")
        if query:
            products = products.filter(Q(name__istartswith=query) | Q(description__icontains=query))
        if category:
            products = products.filter(category__name__istartswith=category)
        products = products.order_by("-created")

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)

        elapsed_ms = (self._timer() - start) * 1000
        timeout_threshold = getattr(settings, "PRODUCT_SEARCH_TIMEOUT_MS", 5000)
        if elapsed_ms > timeout_threshold:
            return Response(
                {
                    "error": "SEARCH_TIMEOUT",
                    "message": f"Search exceeded {timeout_threshold}ms (took {elapsed_ms:.0f}ms)",
                },
                status=408,
            )

        response = paginator.get_paginated_response(serializer.data)
        response.data["elapsed_ms"] = round(elapsed_ms, 2)
        return response


class AuthPingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"user": request.user.username})

