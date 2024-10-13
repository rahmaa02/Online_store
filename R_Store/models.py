from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',max_length=255,unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):

    BISCUITS = 'biscuits'
    MILK =  'milk'
    BREAD =  'bread'

    CATEGORY_CHOICES = [ (BISCUITS, 'Печенье'), (MILK, 'Молочные'), (BREAD, 'Хлебные'),]



    name = models.CharField(verbose_name='Название товара', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name='Описание', blank=True)
    stock = models.PositiveIntegerField(verbose_name='Количество на складе')
    category = models.CharField(verbose_name='Категория', max_length=10, choices=CATEGORY_CHOICES, default=BISCUITS)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение товара', blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_discount_price(self, discount_percentage):
        return self.price - (self.price * discount_percentage / 100)

    def get_full_info(self):
        return f'Товар -- {self.name}, Цена -- {self.price}, Осталось на складе -- {self.stock}'


class User(models.Model):
    username = models.CharField(verbose_name='Имя пользователя', max_length=255, unique=True)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=64)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'User -- {self.username}, {self.email}'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, verbose_name='Товары', related_name='orders')
    total_price = models.DecimalField(verbose_name='Общая стоимость', max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заказ #{self.id} от {self.user}'


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(verbose_name='Оценка', choices=[(i, str(i)) for i in range(1, 6)], default=5)
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Отзыв от {self.user} на {self.product}'

    def commentary(self):
        return self.comment[:10]