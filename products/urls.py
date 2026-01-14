from django.urls import path

from .views import AuthPingAPIView, ProductSearchAPIView

app_name = "products"

urlpatterns = [
    path("products/search/", ProductSearchAPIView.as_view(), name="search"),
    path("auth/ping/", AuthPingAPIView.as_view(), name="auth-ping"),
]
