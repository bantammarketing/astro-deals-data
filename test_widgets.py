#!/usr/bin/env python3
"""
Test script to verify widget JSON files are accessible and contain valid data.
"""

import json
import os
import requests
from datetime import datetime

def test_local_json_files():
    """Test local JSON files for validity and content."""
    stores = ['wags_ann_arbor', 'wags_chelsea', 'wags_ludington', 'wags_tecumseh']
    
    print("🔍 Testing Local JSON Files...")
    print("=" * 50)
    
    for store in stores:
        filename = f"deals_{store}.json"
        
        if not os.path.exists(filename):
            print(f"❌ {filename} - FILE NOT FOUND")
            continue
            
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            if not isinstance(data, list):
                print(f"❌ {filename} - INVALID FORMAT (not a list)")
                continue
                
            deal_count = len(data)
            print(f"✅ {filename} - {deal_count} deals found")
            
            if deal_count > 0:
                # Check first deal structure
                first_deal = data[0]
                required_fields = ['brand', 'title', 'image', 'validity']
                missing_fields = [field for field in required_fields if field not in first_deal]
                
                if missing_fields:
                    print(f"   ⚠️  Missing fields: {missing_fields}")
                else:
                    print(f"   ✅ Valid structure")
                    
        except json.JSONDecodeError as e:
            print(f"❌ {filename} - INVALID JSON: {e}")
        except Exception as e:
            print(f"❌ {filename} - ERROR: {e}")
    
    print()

def test_github_raw_urls():
    """Test GitHub raw URLs for accessibility."""
    stores = ['wags_ann_arbor', 'wags_chelsea', 'wags_ludington', 'wags_tecumseh']
    
    print("🌐 Testing GitHub Raw URLs...")
    print("=" * 50)
    
    for store in stores:
        url = f"https://raw.githubusercontent.com/ryancaravalho/astro-deals-data/main/deals_{store}.json"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                deal_count = len(data) if isinstance(data, list) else 0
                print(f"✅ {store} - {deal_count} deals (Status: {response.status_code})")
            else:
                print(f"❌ {store} - HTTP {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ {store} - Network error: {e}")
        except json.JSONDecodeError as e:
            print(f"❌ {store} - Invalid JSON: {e}")
        except Exception as e:
            print(f"❌ {store} - Error: {e}")
    
    print()

def test_widget_html_files():
    """Test widget HTML files exist and are accessible."""
    stores = ['ann_arbor', 'chelsea', 'ludington', 'tecumseh']
    
    print("📱 Testing Widget HTML Files...")
    print("=" * 50)
    
    for store in stores:
        filename = f"widget_{store}.html"
        
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            print(f"✅ {filename} - {file_size:,} bytes")
        else:
            print(f"❌ {filename} - FILE NOT FOUND")
    
    print()

def main():
    """Run all tests."""
    print("🧩 Wags to Wiskers Deals Widget Test Suite")
    print("=" * 60)
    print(f"Test run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    test_local_json_files()
    test_github_raw_urls()
    test_widget_html_files()
    
    print("🎉 Test suite completed!")
    print("\nNext steps:")
    print("1. If all tests pass, you're ready to launch!")
    print("2. Use the embed codes in squarespace_embed_codes.md")
    print("3. Test the GitHub Actions workflow manually")
    print("4. Deploy widgets to Squarespace pages")

if __name__ == "__main__":
    main() 