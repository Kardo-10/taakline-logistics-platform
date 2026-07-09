import csv

file_path = "data/clean_orders.csv"

monthly_revenue = {}

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        month = f"{row['order_month']} {row['order_year']}"
        revenue = float(row["total_amount"])

        monthly_revenue[month] = monthly_revenue.get(month, 0) + revenue

print("\nMonthly Revenue:\n")

for month, revenue in monthly_revenue.items():
    print(f"{month}: ${revenue:,.2f}")