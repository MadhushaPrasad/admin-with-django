from django.db import models

# Create your models here.


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name="+")


class Product(models.Model):
    # sku = models.CharField(max_length=255, unique=True,primary_key=True)  # varchar(255)
    title = models.CharField(max_length=255)  # varchar(255)
    description = models.TextField()  # text
    price = models.DecimalField(
        max_digits=6, decimal_places=2)  # decimal(6,2)
    inventory = models.IntegerField()  # int
    last_updated = models.DateTimeField(auto_now_add=True)  # timestamp
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"
    MEMBERSHIP_CHOICES = [(MEMBERSHIP_BRONZE, "Bronze"),
                          (MEMBERSHIP_SILVER, "Silver"), (MEMBERSHIP_GOLD, "Gold")]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):

    PAYMENT_PENDING = "P"
    PYAMENT_COMPLETE = "C"
    PAYMENT_FAILED = "F"

    PAYEMNT_STATES_CHOICES = [
        (PAYMENT_PENDING, "Pending"),
        (PYAMENT_COMPLETE, "Complete"),
        (PAYMENT_FAILED, "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=20, choices=PAYEMNT_STATES_CHOICES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, primary_key=True)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
