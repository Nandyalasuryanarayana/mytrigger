from django.test import TestCase

from django.urls import reverse

# Create your tests here.

class BlogViewsTest(TestCase):

    def test_home_view(self):
        # Get response from the home page
        response = self.client.get(reverse('home'))

        # Check if the page loads successfully (HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Check if the correct text is displayed
        self.assertContains(response, "Hello, Django!")