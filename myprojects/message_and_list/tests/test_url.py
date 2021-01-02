from django.test import SimpleTestCase
from django.urls import reverse, resolve

from message_and_list.views import (
    home, next_page, home_view,
    about_view, ProductList
)


class TestUrls(SimpleTestCase):

    def test_first_url_is_resolve(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_next_page_is_resolve(self):
        url = reverse('next_page')
        print(resolve(url))
        self.assertEqual(resolve(url).func, next_page)

    def test_home_view_is_resolve(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_view)

    def test_about_is_resove(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about_view)

    def test_product_list_is_resolved(self):
        url = reverse('product_list')
        self.assertEqual(resolve(url).func.view_class, ProductList)
