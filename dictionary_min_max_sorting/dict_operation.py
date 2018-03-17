stocks = {
    "Google": 520.54,
    "FB": 80.90,
    "Whatsapp": 50.90,
    "Insta": 40.90,
    "Yahoo": 39.80
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))