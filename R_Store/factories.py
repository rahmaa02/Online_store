import factory
from factory.django import ImageField

from R_Store.models import Category, Product, User, Order, Review

class CategoryFactory(factory.django.DjangoModelFactory):
    name =  factory.Faker('word')
    description = factory.Faker('sentence')

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    price = factory.Faker('random_number', digits=5)
    description = factory.Faker('sentence')
    stock = factory.Faker('random_int', min=0, max=100)
    category = factory.Iterator(['biscuits', 'milk', 'bread'])
    image = factory.django.ImageField()

    class Meta:
        model = Product


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    total_price = factory.Faker('random_number', digits=5)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.products.add(product)

    class Meta:
        model = Order


class ReviewFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    rating = factory.Faker('random_int', min=1, max=5)
    comment = factory.Faker('sentence')

    class Meta:
        model = Review