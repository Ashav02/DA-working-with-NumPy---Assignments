

import numpy as np

#the prices of 5 food items on Zomato 

prices = np.array([250,225,275,300,350])

#discounts in rupees

discount_in_rupees = np.array([10,50,60,70,80])

#Element-wise subtraction

final_price = prices - discount_in_rupees
print("Final Price: ",final_price)