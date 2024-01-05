from functools import reduce

transactions = [
    {"product": "Buku", "price": 10000, "quantity": 2},
    {"product": "Pensil", "price": 2000, "quantity": 5},
    {"product": "Pensil", "price": 2000, "quantity": 3},
    {"product": "Pulpen", "price": 5000, "quantity": 2},
    {"product": "Buku", "price": 12000, "quantity": 1},
    {"product": "Pulpen", "price": 6000, "quantity": 4}
]

calculate_transaction_total = lambda transaction: transaction["price"] * transaction["quantity"]

def filter_transactions_by_product(product_name):
    return filter(lambda transaction: transaction["product"] == product_name, transactions)

product_filter_input = input("Masukkan nama produk yang ingin disaring: ")

filtered_transactions = filter_transactions_by_product(product_filter_input)

total_prices = list(map(calculate_transaction_total, filtered_transactions))

total_income = reduce(lambda x, y: x + y, total_prices)

print(f"Transaksi Pembelian Produk {product_filter_input}:")
for transaction in filter_transactions_by_product(product_filter_input):
    print(transaction)

print("\nTotal Harga untuk Setiap Transaksi Produk", product_filter_input + ":")
for price in total_prices:
    print(price)

print("\nTotal Pendapatan dari Transaksi Produk", product_filter_input + ":", total_income)

print("Total Jumlah Item Terjual dari Produk", product_filter_input + ":", sum([transaction["quantity"] for transaction in filter_transactions_by_product(product_filter_input)]))
