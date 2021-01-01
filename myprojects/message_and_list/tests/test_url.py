from django.test import SimpleTestCase
from django.urls import reverse, resolve

from message_and_list.views import home, next_page


class TestUrls(SimpleTestCase):

    def test_first_url_is_resolve(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_next_page_is_resolve(self):
        url = reverse('next_page')
        print(resolve(url))
        self.assertEqual(resolve(url).func, next_page)
