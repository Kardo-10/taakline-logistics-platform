import csv

file_path = "data/clean_orders.csv"

revenue = {}
orders = {}

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        month = f"{row['order_month']} {row['order_year']}"
        amount = float(row["total_amount"])

        revenue[month] = revenue.get(month, 0) + amount
        orders[month] = orders.get(month, 0) + 1

print("\nAverage Order Value:\n")

for month in revenue:
    average = revenue[month] / orders[month]
    print(f"{month}: ${average:,.2f}")