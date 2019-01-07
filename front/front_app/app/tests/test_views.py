from unittest import TestCase
from app.views import Home

class HomeTest(TestCase):
    def setUp(self):
        self.view = Home()

    def test_home_view_returns_listing(self):
        self.assertNotEquals(view.listing, None)