import logging
import googlemaps

# -----------------------------------------------------------------------------

class GeoLocation():
    """
    Abstract class containing geo-location methods
    """
    def __init__(self, api_key):
        self.api_key = api_key
        
    def getLatLong(self, address):
        raise NotImplementedError("Subclass must implement abstract method")
    

class GoogleMapsGeoLocation(GeoLocation):
    """
    Google maps geo location class inherited from GeoLocation class.
    Contains utilities to fetch data from Google Map APIs
    """
    
    def getLatLong(self, address):
        """
        Method to get latitude, longitude from given address from Google MAP APIs
        @param address: address for which latitude and longitude are to be fetched
        """
        
        # Opening connection to Google Map API
        gmaps = googlemaps.Client(self.api_key)
        
        # Getting geo info from address
        geo_info = gmaps.geocode(address)
        
        # Empty response received from Google Map's geo info API
        if not geo_info:
            return None, None
        
        # Returns latitude, longitude from api response
        return geo_info[0]['geometry']['location']['lat'], geo_info[0]['geometry']['location']['lng']
        
class BingMapsGeoLocation(GeoLocation):
    """
    Bing maps geo location class inherited from GeoLocation class.
    Contains utilities to fetch data from Bing Map APIs
    """
    
    def getLatLong(self, address):
        
        #NOTE: Implement bing get location API here
        pass