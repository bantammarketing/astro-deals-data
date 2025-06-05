# 🧩 Astro Loyalty Deals Scraper & JSON Widget

**Version:** 1.0  
**Last Updated:** June 5, 2025  
**Author:** Ryan Caravalho  
**Purpose:** Automate scraping of monthly Astro Loyalty deals from public-facing pet store pages and output as structured JSON for front-end widgets.

---

## 🎯 Goal

Build a Python-based scraper that:
- Loads the deals page (JavaScript-rendered)
- Extracts brand names, offers, image URLs, and validity dates
- Outputs a clean `deals.json` file
- Powers a front-end widget for display on Squarespace sites

---

## 🛠️ Technologies Used

- `Selenium` – for browser automation and rendering JavaScript
- `BeautifulSoup` – for HTML parsing
- `json` – built-in Python module to save structured data
- `urllib.parse.urljoin` – ensures image URLs are absolute

---

## ⚙️ Script Workflow

1. **Open the Deals Page**
   - Uses Selenium with headless Chrome to load the fully rendered page

2. **Wait for Content**
   - Includes a 5-second delay to allow JavaScript-rendered elements to load

3. **Parse HTML**
   - BeautifulSoup parses the page source

4. **Extract Data**
   - For each `.offer_box`, the script extracts:
     - **Brand name**
     - **Offer title**
     - **Image URL** (if available)
     - **Validity date range** (when present)

5. **Save Data**
   - Outputs all deals as a list of dictionaries to `deals.json`

6. **Debugging Support**
   - Saves full rendered HTML to `page_rendered.html` to help troubleshoot parsing issues

---

## 🔍 Key Decisions & Nuances

- **Headless Browser:** Required for pages rendered dynamically with JavaScript
- **Image URL Handling:** Uses `urljoin` to handle relative paths cleanly
- **Validity Parsing:** Searches for "Offer Valid:" strings and extracts ranges, defaulting to empty if missing
- **Error Resilience:** Handles missing values (e.g., brand, title, image) gracefully with fallback defaults

---

## 📁 Output Format (`deals.json`)

```json
[
  {
    "brand": "Farmina",
    "description": "$10 OFF large bags of dry food",
    "image": "https://example.com/image.jpg",
    "validity": "June 1–30"
  },
  ...
]
