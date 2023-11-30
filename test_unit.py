import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = app.test_client()

    def test_index(self):
        # Test the index route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Genre-based Story Generator", response.data)

if __name__ == '__main__':
    unittest.main()
