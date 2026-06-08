daily_sales = [5, 12, 12, 7, 4, 34, 56, 78, 988]
total = sum(sale for sale in daily_sales if sale > 60)
# <generator object <genexpr> at 0x10da72b50>
print(total)
