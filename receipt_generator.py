import cv2
import numpy as np
import random

# Predefined sample receipt items
ITEMS = [
    "Milk", "Eggs", "Bread", "Yogurt", "Juice", 
    "Cheese", "Butter", "Chicken", "Fish", "Vegetables"
]

def generate_random_price():
    """Generates a random price between $1.00 and $10.00 for each item."""
    return round(random.uniform(1.00, 10.00), 2)

def generate_receipt_text():
    """Creates a formatted receipt text with random prices."""
    receipt_text = "SuperMart Receipt\n-------------------------\n"
    total_price = 0.0

    for item in ITEMS:
        price = generate_random_price()
        receipt_text += f"{item:<12} ${price:.2f}\n"
        total_price += price

    receipt_text += "-------------------------\n"
    receipt_text += f"Total:       ${total_price:.2f}\n"
    receipt_text += "Thank you for shopping!\n"
    
    return receipt_text

def generate_receipt_image():
    """Creates a simple black-and-white receipt image with random prices."""
    receipt_text = generate_receipt_text()
    width, height = 400, 500
    image = np.ones((height, width), dtype=np.uint8) * 255  # White background
    font = cv2.FONT_HERSHEY_SIMPLEX
    y_offset = 20

    for line in receipt_text.split("\n"):
        cv2.putText(image, line, (10, y_offset), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        y_offset += 20

    filename = "sample_receipt.png"
    cv2.imwrite(filename, image)
    print(f"✅ Receipt saved as {filename}")

# Generate receipt image
if __name__ == "__main__":
    generate_receipt_image()
