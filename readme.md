# 🧩 Astro Loyalty Deals Scraper & JSON Widget

**Version:** 2.0  
**Last Updated:** January 2025  
**Author:** Ryan Caravalho  
**Purpose:** Automate scraping of monthly Astro Loyalty deals from public-facing pet store pages and output as structured JSON for front-end widgets.

---

## 🎯 Goal

Build a Python-based scraper that:
- Loads the deals page (JavaScript-rendered) for all 4 Wags to Wiskers locations
- Extracts brand names, offers, image URLs, and validity dates
- Outputs clean JSON files for each store
- Powers responsive front-end widgets for display on Squarespace sites
- Automatically updates daily via GitHub Actions

---

## 🛠️ Technologies Used

- `Selenium` – for browser automation and rendering JavaScript
- `BeautifulSoup` – for HTML parsing
- `json` – built-in Python module to save structured data
- `urllib.parse.urljoin` – ensures image URLs are absolute
- `GitHub Actions` – for automated daily updates

---

## 📍 Store Locations

- **Ann Arbor** - `wags_ann_arbor`
- **Chelsea** - `wags_chelsea` 
- **Ludington** - `wags_ludington`
- **Tecumseh** - `wags_tecumseh`

---

## ⚙️ Script Workflow

1. **Batch Scraping**
   - `batch_scrape_stores.py` processes all 4 stores
   - Creates individual JSON files: `deals_wags_[location].json`

2. **Individual Store Scraping**
   - `astro_selenium_scraper.py` handles single store scraping
   - Uses Selenium with headless Chrome to load fully rendered pages

3. **Data Extraction**
   - For each `.offer_box`, extracts:
     - **Brand name**
     - **Offer title**
     - **Image URL** (if available)
     - **Validity date range** (when present)

4. **Output**
   - Saves deals as structured JSON for each store
   - Includes debugging HTML for troubleshooting

---

## 🚀 Launch Instructions

### For Immediate Launch:

1. **Test the GitHub Actions workflow:**
   ```bash
   # Go to GitHub repository
   # Navigate to Actions tab
   # Click "Run workflow" to test the automated scraping
   ```

2. **Deploy widgets to Squarespace:**
   - Use the embed codes in `squarespace_embed_codes.md`
   - Add Code blocks to your Squarespace pages
   - Test each widget on desktop and mobile

3. **Verify automatic updates:**
   - Check that the workflow runs daily at 8:00 UTC
   - Monitor that JSON files are updated automatically
   - Confirm widgets refresh with new data

### Widget Features:
- ✅ **Responsive design** - works on all devices
- ✅ **Auto-refresh** - updates every 30 minutes
- ✅ **Error handling** - graceful fallbacks
- ✅ **Loading states** - user-friendly experience
- ✅ **Last updated timestamp** - shows data freshness

---

## 🔍 Key Decisions & Nuances

- **Headless Browser:** Required for pages rendered dynamically with JavaScript
- **Image URL Handling:** Uses `urljoin` to handle relative paths cleanly
- **Validity Parsing:** Searches for "Offer Valid:" strings and extracts ranges
- **Error Resilience:** Handles missing values gracefully with fallback defaults
- **Multi-store Support:** Individual JSON files for each location

---

## 📁 Output Format (`deals_[store].json`)

```json
[
  {
    "brand": "Farmina",
    "title": "$10 OFF large bags of dry food",
    "image": "https://example.com/image.jpg",
    "validity": "June 1–30"
  },
  ...
]
```

---

## 🔧 GitHub Actions Workflow

The automated workflow (`/.github/workflows/scrape.yml`):
- **Runs daily at 8:00 UTC**
- **Scrapes all 4 stores**
- **Updates JSON files automatically**
- **Commits changes to repository**

### Troubleshooting Workflow Issues:
1. Check Actions tab for error logs
2. Verify Chrome/ChromeDriver installation
3. Ensure repository permissions are set correctly
4. Test manually with `workflow_dispatch`

---

## 📱 Widget Deployment

### Quick Start:
1. Copy embed code from `squarespace_embed_codes.md`
2. Paste into Squarespace Code block
3. Adjust height as needed
4. Test on mobile and desktop

### Customization:
- Modify colors in widget CSS
- Adjust refresh intervals
- Change layout/grid settings
- Add custom branding elements

---

## 🐛 Debugging

- **HTML Debug:** Check `page_rendered.html` for parsing issues
- **Workflow Logs:** Review GitHub Actions for automation problems
- **Widget Issues:** Test individual JSON files in browser
- **Network Problems:** Verify raw.githubusercontent.com access

---

## 📞 Support

For issues with:
- **Scraping:** Check Selenium/Chrome setup
- **Widgets:** Verify JSON file accessibility
- **Automation:** Review GitHub Actions permissions
- **Squarespace:** Test embed codes in different browsers
