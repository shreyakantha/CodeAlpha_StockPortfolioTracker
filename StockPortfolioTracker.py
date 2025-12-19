stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330
}

portfolio = []
total_investment = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not available. Please try another.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a positive integer.")
        continue
    
    price = stock_prices[stock]
    value = quantity * price
    total_investment += value
    portfolio.append((stock, quantity, price, value))
    print(f"Added: {stock} - {quantity} shares at ${price} each = ${value}")


print(f"\nTotal Investment: ${total_investment}")

save = input("Save results to a file? (y/n): ").lower()
if save == 'y':
    filename = input("Enter filename (without extension): ")
    format_choice = input("Save as .txt or .csv? ").lower()
    
    if format_choice == 'txt':
        with open(filename + '.txt', 'w') as f:
            f.write(f"Total Investment: ${total_investment}\n\n")
            f.write("Portfolio Details:\n")
            for stock, qty, pr, val in portfolio:
                f.write(f"{stock}: {qty} shares at ${pr} each = ${val}\n")
        print(f"Results saved to {filename}.txt")
    
    elif format_choice == 'csv':
        import csv
        with open(filename + '.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
            for stock, qty, pr, val in portfolio:
                writer.writerow([stock, qty, pr, val])
            writer.writerow(["Total Investment", "", "", total_investment])
        print(f"Results saved to {filename}.csv")
    
    else:
        print("Invalid format. Results not saved.")
else:
    print("Results not saved.")
