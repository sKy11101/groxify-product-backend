from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category, Product

class ProductApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Vegetables")
        Product.objects.create(
            category=self.category, name="Tomato",
            price=Decimal("40.00"), stock=10, is_active=True
        )

    def test_products_list_is_public(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["name"], "Tomato")

    def test_health_endpoint(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "ok")
