import heapq

grades = [22, 45, 78, 90, 66, 77, 80]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'Appl', 'price': 201},
    {'ticker': 'FB', 'price': 2001},
    {'ticker': 'Insta', 'price': 21},
    {'ticker': 'Watsapp', 'price': 111},
    {'ticker': 'Viber', 'price': 51},
]
print(heapq.nsmallest(2, stocks, key=lambda stocks: stocks['price']))