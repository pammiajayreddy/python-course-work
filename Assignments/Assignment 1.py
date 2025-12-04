print("WELCOME TO D-MART STORE")
print("-----------------------------------")
item_id = int(input("Enter Item ID: "))
item_name = input("Enter Item Name: ")
item_price = float(input("Enter Item Price: "))
categories = input("Enter Item Categories (separate items with commas): ")
item_categories = categories.split(",")

item_stock = float(input("Enter Stock Availability Percentage: "))

discount_input = input("Enter Available Discounts (separate discounts of each product with commas): ")
discount_list = discount_input.split(",")
sold_units = int(input("Enter Sold Units: "))
total_units = int(input("Enter Total Units Available: "))
stock_tuple = (sold_units, total_units)
brands_raw = input("Enter Brands Available (separate brands with commas): ")
brand_set = set(brands_raw.split(","))
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Email: ")
supplier_location = input("Enter Supplier Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}
print("\nD-Mart Item Information:")
print("-----------------------------------")
print("Item ID, Name, Price:", item_id, item_name, item_price, sep=", ")
print("Stock Availability: %.2f%%" % item_stock)
print(f"Item Name: {item_name}")
print(f"Price: ₹{item_price:.2f}")
print(f"Discount Options: {discount_list}")
print(f"Units Sold: {stock_tuple[0]} out of {stock_tuple[1]}")
print(f"Brands Available: {brand_set}")
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details["name"],
    supplier_details["contact"],
    supplier_details["location"]
))

print("-----------------------------------")
