from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class SimpleTest(TestCase):
    def test1(self):
        # This test will pass because 1 + 1 == 2
        self.assertEqual(1 + 1, 2)
