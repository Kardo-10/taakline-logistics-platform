import csv

file_path = "data/clean_orders.csv"

customer_revenue = {}

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        customer = row["customer_name"]
        amount = float(row["total_amount"])

        customer_revenue[customer] = (
            customer_revenue.get(customer, 0) + amount
        )

sorted_customers = sorted(
    customer_revenue.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Customers By Revenue:\n")

for customer, revenue in sorted_customers[:10]:
    print(f"{customer}: ${revenue:,.2f}")