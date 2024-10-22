from django.urls import reverse

from django.test import TestCase
from R_Store import factories, models

# Create your tests here.


class RStoreTestCase(TestCase):
    def setUp(self):
        self.category = models.Category.objects.create(name='biscuits', description='Test category')
        self.product = models.Product.objects.create(name='Manual Test Product', price=100.00, description='This is a manually created product', stock=50,category=self.category.name, image=None)

    def test_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), models.Product.objects.count())

    def test_create_product(self):
        initial_product_count = models.Product.objects.count()

        product_data = { 'name': 'New Test Product', 'price': '100.00', 'description': 'This is a test product', 'stock': 50, 'category': 'biscuits',}
        response = self.client.post(reverse('product-create'), data=product_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Product.objects.count(), initial_product_count + 1)

        new_product = models.Product.objects.last()
        self.assertEqual(new_product.name, product_data['name'])
        self.assertEqual(float(new_product.price), float(product_data['price']))
        self.assertEqual(new_product.description, product_data['description'])
        self.assertEqual(new_product.stock, product_data['stock'])
        self.assertEqual(new_product.category, product_data['category'])


    def test_product_detail(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['product'].pk, self.product.pk)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.price)

    def test_update_product(self):
        old_name = self.product.name
        old_description = self.product.description

        update_data = {'name': 'Updated Product','price': self.product.price,'description': old_description,'stock': self.product.stock,'category': 'bread',}

        url = reverse('product-update', kwargs={'pk': self.product.pk})
        response = self.client.post(url, update_data)

        self.product.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.product.name, old_name)
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(self.product.category, 'bread')

    def test_delete_product(self):
        old_product_count = models.Product.objects.count()
        url = reverse('product-delete', kwargs={'pk': self.product.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        new_product_count = models.Product.objects.count()
        self.assertEqual(new_product_count, old_product_count - 1)