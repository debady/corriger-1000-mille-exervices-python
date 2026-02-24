import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_image_links(url, limit=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Vérifie que la requête est valide
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    image_links = set()  # Utilisation d'un set pour éviter les doublons

    # Recherche des balises <img>
    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("src")  # Prend en compte les images en lazy loading
        if src:
            full_url = urljoin(url, src)  # Convertir en URL absolue
            image_links.add(full_url)
            if len(image_links) >= limit:  # Limite à 10 images
                break

    return list(image_links)

def save_to_json(data, filename="images.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    site_url = input("Entrez l'URL du site : ")
    image_links = get_image_links(site_url)

    if image_links:
        save_to_json(image_links)
        print(f"{len(image_links)} images trouvées. Résultat enregistré dans 'images.json'.")
    else:
        print("Aucune image trouvée.")
