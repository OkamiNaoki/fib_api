from django.test import TestCase
from django.urls import reverse

class FibonacciAPITestCase(TestCase):
    def test_valid_input(self):
        response = self.client.get(reverse('fib'), {'n': 99})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 218922995834555169026})
    
    def test_invalid_input_string(self):
        response = self.client.get(reverse('fib'), {'n': 'abc'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"status": 400,"message": "Bad request."})
    
    def test_invalid_input_negative(self):
        response = self.client.get(reverse('fib'), {'n': -5})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"status": 400,"message": "Invalid Value."})
