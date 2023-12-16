import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calc_date_region_all_avg(df, date, region):
    rows = df[(df['Date'] == date) & (df['Region'] == region)]
    return rows['SalesAmount'].mean()


def calc_date_region_all_sum(df, date, region):
    rows = df[(df['Date'] == date) & (df['Region'] == region)]
    return rows['SalesAmount'].sum()


def plot_date_region_all_SalesQuantity_Inventory(df, date, region):
    rows = df[(df['Date'] == date) & (df['Region'] == region)]
    fig, ax = plt.subplots()
    labels = ['SalesQuantity', 'Inventory']
    bar_width = 0.05
    bar_positions = np.arange(len(labels))
    for index, row in rows.iterrows():
        ax.bar(bar_positions + (index*bar_width), row.loc[labels],
               width=bar_width, label=row['ProductType'])
    plt.xticks(bar_positions + bar_width / 2, labels)
    ax.set_title('Compare Quantity and Inventory of different products')
    ax.legend()
    plt.show()


def calc_date_all_product_avg(df, date, product):
    rows = df[(df['Date'] == date) & (df['ProductType'] == product)]
    return rows['SalesAmount'].mean()


def calc_date_all_product_sum(df, date, product):
    rows = df[(df['Date'] == date) & (df['ProductType'] == product)]
    return rows['SalesAmount'].sum()


def plot_date_all_product_InventoryCarryRate(df, date, product):
    rows = df[(df['Date'] == date) & (df['ProductType'] == product)]
    fig, ax = plt.subplots()
    labels = ['InventoryCarryRate']
    bar_width = 0.5
    bar_positions = np.arange(len(labels))
    for index, row in rows.iterrows():
        ax.bar(bar_positions + (index*bar_width), row['SalesQuantity'] / row['Inventory'],
               width=bar_width, label=row['Region'])
    plt.xticks(bar_positions + bar_width / 2, labels)
    ax.set_title('Compare inventory carry rate of different region')
    ax.legend()
    plt.show()


csv_file_path = 'sales_data.csv'
df = pd.read_csv(csv_file_path)
df['SalesAmount'] = df['Price'] * df['SalesQuantity']

# print(calc_date_region_all_avg(df, '2000-01-01', 'a'))
# print(calc_date_region_all_sum(df, '2000-01-01', 'a'))
# plot_date_region_all_SalesQuantity_Inventory(df, '2000-01-01', 'a')
# print(calc_date_all_product_avg(df, '2000-01-01', 'Books'))
# print(calc_date_all_product_sum(df, '2000-01-01', 'Books'))
# plot_date_all_product_InventoryCarryRate(df, '2000-01-01', 'Books')
