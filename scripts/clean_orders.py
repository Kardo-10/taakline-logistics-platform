import csv
from datetime import datetime

input_file = "data/completed_orders_Jan_1_2024_-_Jul_31_2026.csv"
output_file = "data/clean_orders.csv"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)

    fieldnames = [
        "order_number",
        "customer_name",
        "status",
        "completed_date",
        "order_month",
        "order_year",
        "delivered_date",
        "total_amount",
        "items_count",
        "primary_item"
    ]

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:

        completed_date = row["Completed Date"]

        date_obj = datetime.strptime(
            completed_date,
            "%m/%d/%Y %I:%M %p"
        )

        writer.writerow({
            "order_number": row["Order Number"],
            "customer_name": row["Customer Name"],
            "status": row["Status"],
            "completed_date": completed_date,
            "order_month": date_obj.strftime("%B"),
            "order_year": date_obj.year,
            "delivered_date": row["Delivered Date"],
            "total_amount": row["Total Amount"].replace("$", "").replace(",", ""),
            "items_count": row["Items Count"],
            "primary_item": row["Primary Item"]
        })

print("Clean dataset created successfully!")