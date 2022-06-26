# Data points
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Variables
total_price = 0
total_revenue = 0
#  Calculate Average Haircut
for price in prices:
  total_price = price + total_price
  average_price = total_price / len(prices)
   
# Price reduction by $5
new_prices = [price - 5 for price in prices]

# Calculate Total Revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# Calculate Daily Revenue
average_daily_revenue = total_revenue / 7

# Haircuts under $30 by name
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print("Average Haircut Price: "+ str(average_price))
print("Adjusted Haircut Prices: " + str(new_prices))
print("Total Revenue: "+str(total_revenue))
print("Average Daily Revenue: ", str(average_daily_revenue))
print("Haircuts under $30:" + str(cuts_under_30))
