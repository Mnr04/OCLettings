from django.test import TestCase
from django.urls import reverse


class OCLettingsSiteTest(TestCase):

    def test_index_page(self):
        """Test Homepage"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Holiday Homes", response.content)
