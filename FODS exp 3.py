import numpy as np

house_data = np.array([
    [3, 1500, 200000],
    [5, 2500, 350000],
    [4, 2000, 280000],
    [6, 3000, 450000],
    [5, 2700, 400000]
])

filtered = house_data[house_data[:, 0] > 4]

average_price = np.mean(filtered[:, 2])

print("Average Sale Price:", average_price)

