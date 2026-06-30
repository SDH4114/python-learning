import numpy as np
import pandas as pd
import data

total_sales = data.prices * data.quantities
print(f"Total sales - {total_sales}")

total_revenue = np.sum(total_sales)
print(f"Total revenue - {total_revenue}")

average_check = np.mean(total_sales)
print(f"Total check - {average_check}")



# best and worst
best_product_index = np.argmax(total_sales)
worst_product_index = np.argmin(total_sales)

print(best_product_index)
print(f"Best product ID - {data.products_ids[best_product_index]}, sales amount - {total_sales[best_product_index]:.2f}$")

print(f"Worst product ID - {data.products_ids[worst_product_index]}, sales amount - {total_sales[worst_product_index]:.2f}$")


dates_pd = pd.to_datetime(data.dates)
print(f"Sales per week {dates_pd}")
