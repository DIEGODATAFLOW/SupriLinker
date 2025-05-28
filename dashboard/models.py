from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("Escritório e Papelaria", "Escritório e Papelaria"),
    ("Eletrônicos", "Eletrônicos"),
    ("Alimentos", "Alimentos"),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = "Produto"

    def __str__(self):
        return f"{self.name}-{self.quantity}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Pedido"

    def __str__(self):
        return f"{self.product} solicitado por {self.staff.username}"
