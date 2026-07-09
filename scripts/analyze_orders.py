import csv

file_path = "data/completed_orders_Jan_1_2024_-_Jul_31_2026.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Columns:")
    print(reader.fieldnames)

    print("\nFirst 5 Records:")

    for i, row in enumerate(reader):
        if i >= 5:
            break

        print("\nRecord", i + 1)
        print(row)