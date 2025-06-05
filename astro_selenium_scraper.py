from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import time

URL = "https://secure.astroloyalty.com/members.php?ld=xZzugnkcBMFfSCnQA%2Fg%3D"
BASE_URL = "https://secure.astroloyalty.com"

options = Options()
options.add_argument("--headless")  # No browser window
driver = webdriver.Chrome(options=options)

driver.get(URL)
time.sleep(5)  # Wait for JS to load

html = driver.page_source

# Save the rendered HTML for debugging
with open("page_rendered.html", "w") as f:
    f.write(html)

soup = BeautifulSoup(html, "html.parser")
deals = []

for offer in soup.select(".offer_box"):
    img_tag = offer.select_one("img")
    if img_tag and img_tag.get("src"):
        image = urljoin(BASE_URL, img_tag["src"])
        print("Image URL:", image)  # <-- This line prints each image URL found
    else:
        image = ""
        print("No image found for this offer.")
    brand = offer.select_one(".mfg_heading")
    brand = brand.get_text(strip=True) if brand else ""
    title = offer.select_one(".offer_title")
    title = title.get_text(strip=True) if title else ""
    validity = offer.find(string=lambda text: "Offer Valid:" in text)
    if validity:
        validity_span = validity.parent
        dates = validity_span.find_all("br")
        if dates and len(dates) > 0:
            date_range = dates[-1].next_sibling.strip() if dates[-1].next_sibling else ""
        else:
            date_range = ""
    else:
        date_range = ""
    deals.append({
        "brand": brand,
        "title": title,
        "image": image,
        "validity": date_range
    })

with open("deals.json", "w") as f:
    json.dump(deals, f, indent=2)

print("Scraped and saved deals to deals.json")
driver.quit()