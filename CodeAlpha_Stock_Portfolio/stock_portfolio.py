
stock_prices = {
    "AAPL": 150,
    "TSLA": 250,
    "GOOG": 300,
    "AMZN": 350
}# Stock price dictionary

portfolio = {}
total_value = 0
print("-----+-----+-----+-----+-----+-----+-----+-----+")
n = int(input("Enter number of stocks you want to buy: "))

for i in range(n):
    stock = input("Enter stock name (AAPL/TSLA/GOOG/AMZN): ").upper()
    quantity = int(input("Enter quantity: "))
    
    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Stock not available!")
print("-----+-----+-----+-----+-----+-----+-----+-----+")



# Calculate total investment
print("\n--------------- Portfolio Summary ---------------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    
    print(stock, "- Quantity:", quantity, " Price:", price, " Value:", value)

print("Total Investment Value =", total_value)

# Save result in text file
file = open("portfolio.txt", "w")
file.write("Stock Portfolio Summary\n")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    file.write(f"{stock} Quantity:{quantity} Value:{value}\n")

file.write(f"Total Investment Value = {total_value}")
file.close()

print("Portfolio saved in portfolio.txt file")
print("-------------------------------------------------")
