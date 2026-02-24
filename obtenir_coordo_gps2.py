# pip install geocoder geopy gps3 et pip install geocoder geopy requests
import geocoder
from geopy.geocoders import Nominatim
import json
import subprocess

def get_gps_coordinates():
    try:
        # Récupérer l'emplacement basé sur l'adresse IP
        location = geocoder.ip('me')

        if location.latlng:
            latitude, longitude = location.latlng
            altitude = None  # L'IP ne fournit pas l'altitude

            # Obtenir l'adresse approximative avec Geopy
            geolocator = Nominatim(user_agent="geo_locator")
            address = geolocator.reverse((latitude, longitude), exactly_one=True)

            # Récupérer l'altitude en utilisant un service de géolocalisation
            altitude = get_altitude(latitude, longitude)

            # Affichage des coordonnées brutes
            gps_data = {
                "latitude": latitude,
                "longitude": longitude,
                "altitude": altitude if altitude else "Indisponible",
                "adresse": address.address if address else "Indisponible"
            }

            print("\n📍 Vos coordonnées GPS brutes :")
            print(json.dumps(gps_data, indent=4, ensure_ascii=False))

            return gps_data
        
        else:
            print("❌ Impossible de récupérer les coordonnées GPS.")
            return None

    except Exception as e:
        print(f"⚠️ Erreur : {e}")
        return None

def get_altitude(lat, lon):
    """
    Obtenir l'altitude via un service en ligne Open-Elevation.
    """
    try:
        import requests
        url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
        response = requests.get(url)
        if response.status_code == 200:
            elevation_data = response.json()
            return elevation_data["results"][0]["elevation"]
        return None
    except Exception as e:
        print(f"⚠️ Erreur récupération altitude : {e}")
        return None

if __name__ == "__main__":
    get_gps_coordinates()
