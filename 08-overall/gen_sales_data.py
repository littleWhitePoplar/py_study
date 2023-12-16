import csv
import random
from datetime import datetime, timedelta
from itertools import product


def generate_dates(start_date, end_date):
    date_generated = [
        start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]
    return date_generated


def generate_random_data(dates):
    date_format = "%Y-%m-%d"
    regions = [chr(i) for i in range(ord('a'), ord('t') + 1)]
    product_types = ["Electronics", "Clothing", "Books", "Toys",
                     "Furniture", "Appliances", "Sports", "Beauty", "Food", "Jewelry"]

    data = []

    for date in dates:
        for region, product_type in product(regions, product_types):
            sales_quantity = random.randint(10, 100)
            inventory = random.randint(50, 500)
            price = random.uniform(50.0, 200.0)

            data.append([date.strftime(date_format), region,
                        sales_quantity, inventory, price, product_type])

    return data


def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Region",
                        "SalesQuantity", "Inventory", "Price", "ProductType"])
        writer.writerows(data)


if __name__ == "__main__":
    start_date = datetime.strptime("2000-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2019-12-31", "%Y-%m-%d")

    all_dates = generate_dates(start_date, end_date)
    generated_data = generate_random_data(all_dates)
    save_to_csv(generated_data, 'sales_data.csv')
