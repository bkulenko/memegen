from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from unittest.mock import Mock, patch
from app.views import Home, Listing

import django
django.setup()


class HomeTest(TestCase):

    def test_home_view_returns_ok(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "OK")

listing_items = {'uid': 'uid', 'base64_200_thumb': 'test'}


class ListingTest(TestCase):

    def test_listing_returns_items_when_connected_to_db(self):
        response = self.client.get('/listing/')
        self.assertContains(response, 'xd')
