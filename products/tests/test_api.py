from datetime import timedelta
from unittest import mock

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from products.models import Category, Product

User = get_user_model()


class ProductSearchAPITests(APITestCase):
    def setUp(self):
        cache.clear()
        self.category = Category.objects.create(name="Fitness")
        Product.objects.bulk_create(
            [
                Product(
                    name=f"Yoga Mat {i}",
                    category=self.category,
                    price="29.99",
                    description="Eco mat",
                )
                for i in range(5)
            ]
        )

    def test_search_returns_results_under_threshold(self):
        url = reverse("products:product-search")
        from datetime import timedelta
        from unittest import mock

        from django.contrib.auth import get_user_model
        from django.core.cache import cache
        from django.test import override_settings
        from django.urls import reverse
        from rest_framework import status
        from rest_framework.test import APITestCase
        from rest_framework_simplejwt.tokens import RefreshToken

        from products.models import Category, Product

        User = get_user_model()


        class ProductSearchAPITests(APITestCase):
            def setUp(self):
                cache.clear()
                self.category = Category.objects.create(name="Fitness")
                Product.objects.bulk_create(
                    [
                        Product(
                            name=f"Yoga Mat {i}",
                            category=self.category,
                            price="29.99",
                            description="Eco mat",
                        )
                        for i in range(5)
                    ]
                )

            def test_search_returns_results_under_threshold(self):
                url = reverse("products:search")
                with mock.patch("products.views.ProductSearchAPIView._timer", side_effect=[0.0, 0.02]):
                    response = self.client.get(url, {"q": "Yoga"})
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                payload = response.json()
                self.assertIn("results", payload)
                self.assertLessEqual(payload.get("elapsed_ms"), 200)

            @override_settings(PRODUCT_SEARCH_TIMEOUT_MS=50)
            def test_search_timeout_returns_408(self):
                url = reverse("products:search")
                with mock.patch("products.views.ProductSearchAPIView._timer", side_effect=[0.0, 0.10]):
                    response = self.client.get(url, {"q": "Yoga"})
                self.assertEqual(response.status_code, 408)
                self.assertEqual(response.json().get("error"), "SEARCH_TIMEOUT")


        class TokenExpiryTests(APITestCase):
            def setUp(self):
                self.user = User.objects.create_user(username="apiuser", password="pass1234")
                self.url = reverse("products:auth-ping")

            def _auth_header(self, token):
                return {"HTTP_AUTHORIZATION": f"Bearer {token}"}

            def test_valid_token_allows_access(self):
                refresh = RefreshToken.for_user(self.user)
                response = self.client.get(self.url, **self._auth_header(str(refresh.access_token)))
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.json()["user"], self.user.username)

            def test_expired_token_returns_custom_error(self):
                refresh = RefreshToken.for_user(self.user)
                access = refresh.access_token
                access.set_exp(lifetime=timedelta(seconds=-1))
                response = self.client.get(self.url, **self._auth_header(str(access)))
                self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
                payload = response.json()
                self.assertEqual(payload.get("error"), "token_expired")
                self.assertEqual(payload.get("refresh_endpoint"), "/api/token/refresh/")

