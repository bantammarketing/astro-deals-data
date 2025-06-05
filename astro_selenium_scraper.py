from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import time
import sys

def scrape_astro_deals(url, output_json="deals.json"):
    BASE_URL = "https://secure.astroloyalty.com"
    options = Options()
    options.add_argument("--headless")  # No browser window
    driver = webdriver.Chrome(options=options)

    driver.get(url)
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
        else:
            image = ""
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

    with open(output_json, "w") as f:
        json.dump(deals, f, indent=2)

    print(f"Scraped and saved deals to {output_json}")
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python astro_selenium_scraper.py <astro_deals_url> [output_json]")
        sys.exit(1)
    url = sys.argv[1]
    output_json = sys.argv[2] if len(sys.argv) > 2 else "deals.json"
    scrape_astro_deals(url, output_json)