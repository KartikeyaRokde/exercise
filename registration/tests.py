from rest_framework import status
from rest_framework.test import APITestCase
from registration.models import User
from tasks import save_geo_details

class RegistrationTests(APITestCase):
    """
    Unit test cases for User Registration API
    """
    
    def setUp(self):
        self.test_name = 'Test Bot'
        self.test_email = 'testbot@test.com'
        self.test_password = 'test'
        self.test_address = 'Ahmedabad, India'
    
    def test_user_registration(self):
        """
        Test for successful user registration
        """
        
        # Forming user registration request payload
        data = {'name': self.test_name, 'email':self.test_email, 
                'password':self.test_password, 'address':self.test_address}
        
        # Making API call for user registration
        response = self.client.post('/users/registration/', data, format='json')
        
        # Test response code as 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test response user id
        self.assertEqual(User.objects.get(email=self.test_email).id, response.json()['user_id'])
        
        self.user_id = User.objects.get(email=self.test_email).id
        
    def test_user_registration_invalid_data(self):
        """
        Test user registration proper error for invalid data
        """
        
        # Forming user registration request payload with invalid email id
        data = {'name': self.test_name, 'email':self.test_email + '.garbage.com.##$$', 
                'password':self.test_password, 'address':self.test_address}
        
        # Making API call for user registration
        response = self.client.post('/users/registration/', data, format='json')
        
        # Assert for response status 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
