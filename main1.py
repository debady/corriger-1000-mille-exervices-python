import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_image_links(url, limit=10):
    options = Options()
    options.headless = True  # Exécute le navigateur en mode sans interface
    options.add_argument("--disable-blink-features=AutomationControlled")  # Contourne certaines protections
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    # Initialiser Selenium
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Laisse le temps à la page de se charger

        # Récupération du contenu HTML
        soup = BeautifulSoup(driver.page_source, "html.parser")
        image_links = set()

        # Recherche des balises <img>
        for img in soup.find_all("img"):
            src = img.get("data-src") or img.get("src")
            if src:
                full_url = urljoin(url, src)
                image_links.add(full_url)
                if len(image_links) >= limit:
                    break

        return list(image_links)

    except Exception as e:
        print(f"Erreur lors de la récupération des images : {e}")
        return []
    
    finally:
        driver.quit()

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
