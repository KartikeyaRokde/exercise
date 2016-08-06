import os
import logging
from celery import task
from registration.models import User
from geolocation import GoogleMapsGeoLocation #BingMapsGeoLocation

# -----------------------------------------------------------------------------

# Initialize logger
logger = logging.getLogger(__name__)

# Initialize google maps geo location class
geolocation_obj = GoogleMapsGeoLocation(os.environ.get('GOOGLE_API_KEY'))

# NOTE: Change above line to BingMapsGeoLocation to use Bing maps API instead of google maps
#geolocation = BingMapsGeoLocation(os.environ.get('BING_API_KEY'))

@task
def save_geo_details(user_id, address):
    """
        Celery task to save geo details (lat, lng) for user
    """
    # Checking if user with given user_id exists
    try:
        user = User.objects.get(id=user_id)
    except:
        logger.error("SAVE GEO DETAILS: Invalid user_id %s" % user_id)
        return False
    
    if address == None or address == '':
        logger.error("SAVE GEO DETAILS: Invalid address %s" % address)
        return False
    
    try:
        # Getting latitude & longitude for given address
        lat, lng = geolocation_obj.getLatLong(address)
    except Exception as e:
        logger.error("SAVE GEO DETAILS: Error in fetching geo info. Error %s" % e)
        return False
    
    # Saving latitude & longitude for user
    if lat and lng:
        user.lat = lat
        user.lng = lng
        user.save()
    
    # User's geo details saved successfully
    logger.info("SAVE GEO DETAILS: Geo details saved successfully for user %s" % user.email)
    return True
