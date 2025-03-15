import cv2
import pytesseract

# Set the path to your Tesseract installation
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import re
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Predefined receipt item data (item name -> expiry date)
RECEIPT_EXPIRY_DB = {
    "Milk": "2025-03-20",
    "Eggs": "2025-03-25",
    "Bread": "2025-03-18",
    "Yogurt": "2025-03-17",
    "Juice": "2025-03-22",
    "Cheese": "2025-03-15",
    "Butter": "2025-03-30",
    "Chicken": "2025-03-14",
    "Fish": "2025-03-29",
    "Vegetables": "2025-03-16"
}

def extract_text_from_receipt(image_path):
    """Extracts text from a receipt image using OCR."""
    
    # ✅ Fix 1: Ensure the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"❌ Error: File not found at '{image_path}'. Check the file location.")
    
    # ✅ Fix 2: Load image and check if it's valid
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"❌ Error: Unable to load image at '{image_path}'. Ensure it's a valid image format.")
    
    
    # Convert to grayscale and extract text
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    
    return text

def extract_items(text):
    """Finds product names from OCR-extracted text and matches them with expiry dates."""
    items_found = {}
    
    for item in RECEIPT_EXPIRY_DB.keys():
        if item.lower() in text.lower():
            items_found[item] = RECEIPT_EXPIRY_DB[item]
    
    return items_found

def check_expiry(expiry_dict):
    """Checks expiry dates and prints status."""
    today = datetime.today().date()
    
    print("\n📌 Expiry Status of Products:\n")
    
    if not expiry_dict:  # Check if the dictionary is empty
        print("⚠ No items found to check expiry!")
        return

    for product, date_str in expiry_dict.items():
        print(f"🔍 Checking {product} with expiry date: {date_str}")  # Debugging

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
            print(f"⚠ Error parsing date for {product}: {date_str}")


# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\Jacob\Desktop\sample_receipt.png"  # ✅ Ensure the correct file path
    
    try:
        receipt_text = extract_text_from_receipt(image_path)
        print("\n🛒 Extracted Receipt Text:\n", receipt_text)
        
        items_found = extract_items(receipt_text)
        print("\n🛍 Extracted Items & Expiry Dates:\n", items_found)
        
        check_expiry(items_found)
    
    except Exception as e:
        print(f"❌ Error: {e}")
