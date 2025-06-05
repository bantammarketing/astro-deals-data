import json
import subprocess

# Load the list of stores from stores.json
with open('stores.json', 'r') as f:
    stores = json.load(f)

for store in stores:
    name = store['name']
    url = store['url']
    output_file = f"deals_{name}.json"
    print(f"Scraping {name}...")
    # Call the scraper script for each store
    subprocess.run([
        "python", "astro_selenium_scraper_any.py", url, output_file
    ])
print("All stores scraped!")
