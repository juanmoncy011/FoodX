import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

# Predefined barcode data (barcode -> item name & expiry date)
BARCODE_EXPIRY_DB = {
    "0123456789012": {"item_name": "Milk", "expiry_date": "2025-03-20"},
    "9876543210987": {"item_name": "Eggs", "expiry_date": "2025-03-25"},
    "5558887776665": {"item_name": "Bread", "expiry_date": "2025-03-18"},
    "3332221110009": {"item_name": "Yogurt", "expiry_date": "2025-03-17"},
    "8887776665554": {"item_name": "Juice", "expiry_date": "2025-03-22"},
    "6665554443332": {"item_name": "Cheese", "expiry_date": "2025-03-15"},
    "4443332221111": {"item_name": "Butter", "expiry_date": "2025-03-30"},
    "2221110009998": {"item_name": "Chicken", "expiry_date": "2025-03-14"},
    "1110009998887": {"item_name": "Fish", "expiry_date": "2025-03-29"},
    "9998887776666": {"item_name": "Vegetables", "expiry_date": "2025-03-16"}
}

def scan_barcodes(image_path):
    """Scans barcodes from an image and returns detected item details."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray)
    
    scanned_items = {}
    for barcode in barcodes:
        barcode_text = barcode.data.decode("utf-8")
        item_info = BARCODE_EXPIRY_DB.get(barcode_text, {"item_name": "Unknown", "expiry_date": "Unknown"})
        scanned_items[item_info["item_name"]] = item_info["expiry_date"]
    
    return scanned_items

def check_expiry(expiry_dict):
    """Checks expiry dates and prints status."""
    today = datetime.today().date()
    
    print("\n📌 Expiry Status of Products:\n")
    for product, date_str in expiry_dict.items():
        try:
            expiry_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            days_left = (expiry_date - today).days
            if days_left == 0:
                print(f"⚠ ALERT: {product} expires TODAY!")
            elif days_left > 0:
                print(f"✅ {product} is fresh. Expires in {days_left} days.")
            else:
                print(f"❌ {product} has EXPIRED! Expired {-days_left} days ago.")
        except ValueError:
            print(f"⚠ Could not parse date for {product}: {date_str}")

# Example usage
if __name__ == "__main__":
    image_path = "sample_barcode.png"  # Change to actual barcode image path
    scanned_items = scan_barcodes(image_path)
    
    print("\n🔍 Scanned Items & Expiry Dates:\n", scanned_items)
    check_expiry(scanned_items)
