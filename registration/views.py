# Library imports
import logging
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

# Application imports
from registration.models import User
from serializers import UserRegistrationSerializer
from tasks import save_geo_details

# -----------------------------------------------------------------------------

# Initialize logger
logger = logging.getLogger(__name__)


@api_view(["POST"])
@parser_classes((JSONParser,JSONRenderer),)
def user_registration(request):
    """
        End-point for user registration
    """
    
    # Validating data through serializer
    serializer = UserRegistrationSerializer(data = request.data)
    if not serializer.is_valid():
        
        logger.debug('USER REGISTRATION: Invalid data. Errors: %s' % serializer.errors)
        # Return error response if request data is invalid
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Creating User instance and assigning data
    user = User()
    user.name = serializer.data['name']
    user.email = serializer.data['email']
    user.password = make_password(serializer.data['password'])
    user.address = serializer.data['address']
    
    # Saving user object to database
    try:
        user.save()
        logger.info("USER REGISTRATION: User object saved successfully. \
                        User email: %s, User ID: %s" % (user.email, user.id))
    except Exception as e:
        logger.debug("USER REGISTRATION: User already registered with email id %s. \
                        Error: %s" % (serializer.data['email'], e))
        return Response({'detail':'User already registered with the provided email'}, 
                        status = status.HTTP_400_BAD_REQUEST)
    
    # Calling save geo details task to run in background
    save_geo_details.apply_async([user.id, serializer.data['address']])
    
    return Response({'message':'User registered successfully', 'user_id':user.id},
                    status=status.HTTP_201_CREATED)
