import csv

file_path = "data/clean_orders.csv"

orders_by_month = {}

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = f"{row['order_month']} {row['order_year']}"

        orders_by_month[month] = orders_by_month.get(month, 0) + 1

print("\nOrders by Month:\n")

for month, orders in orders_by_month.items():
    print(f"{month}: {orders} orders")