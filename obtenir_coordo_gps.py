# import geocoder et pip install geocoder geopy requests
import geocoder
from geopy.geocoders import Nominatim

def get_gps_coordinates():
    try:
        # Récupérer l'emplacement basé sur l'IP
        location = geocoder.ip('me')
        
        if location.latlng:
            latitude, longitude = location.latlng
            print(f"📍 Vos coordonnées GPS approximatives :")
            print(f"Latitude : {latitude}")
            print(f"Longitude : {longitude}")
            
            # Récupérer plus d'infos avec geopy
            geolocator = Nominatim(user_agent="geo_locator")
            address = geolocator.reverse((latitude, longitude), exactly_one=True)
            
            if address:
                print(f"📌 Adresse approximative : {address.address}")
            else:
                print("🔍 Impossible de récupérer l'adresse exacte.")
        else:
            print("❌ Impossible de récupérer les coordonnées GPS.")
    
    except Exception as e:
        print(f"⚠️ Erreur : {e}")

if __name__ == "__main__":
    get_gps_coordinates()
