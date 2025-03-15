import barcode
from barcode.writer import ImageWriter

# Predefined barcode data (Full 13-digit barcodes)
BARCODE_DATA = {
    "Milk": "0123456789012",
    "Eggs": "9876543210987",
    "Bread": "5558887776665",
    "Yogurt": "3332221110009",
    "Juice": "8887776665554",
    "Cheese": "6665554443332",
    "Butter": "4443332221111",
    "Chicken": "2221110009998",
    "Fish": "1110009998887",
    "Vegetables": "9998887776666"
}

def generate_barcode(item_name, barcode_number):
    """Generates a barcode image for a given item using Code128."""
    code128 = barcode.get_barcode_class('code128')  # Use Code128 to preserve 13 digits
    barcode_instance = code128(barcode_number, writer=ImageWriter())
    filename = f"{item_name.replace(' ', '_')}_barcode"
    barcode_instance.save(filename)  # Saves as PNG
    print(f"✅ Barcode saved as {filename}.png with barcode: {barcode_number}")

# Generate all barcodes
if __name__ == "__main__":
    for item, barcode_number in BARCODE_DATA.items():
        generate_barcode(item, barcode_number)
