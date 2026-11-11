''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
15. Create a pie chart using Matplotlib to show the market share percentage of five smartphone brands. Ensure the chart includes a legend and percentage labels. '''

import matplotlib.pyplot as plt

brands = ["Samsung", "Apple", "Xiaomi", "Vivo", "Oppo"]
shares = [30, 25, 20, 15, 10]

plt.pie(shares, labels=brands, autopct="%1.1f%%", startangle=140)

plt.title("Market Share of Smartphone Brands")
plt.legend(brands, title="Brands", loc="upper right")

plt.show()
