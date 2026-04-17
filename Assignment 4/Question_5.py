'''
This program reads health_data.csv and makes scatter plots.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("health_data.csv")

plt.figure(figsize=(15,10))

plt.subplot(2,3,1)
plt.scatter(df['weight'], df['height'])
plt.title("weight vs height")

plt.subplot(2,3,2)
plt.scatter(df['age'], df['weight'])
plt.title("age vs weight")

plt.subplot(2,3,3)
plt.scatter(df['height'], df['age'])
plt.title("height vs age")

plt.subplot(2,3,4)
plt.scatter(df['gender'], df['height'])
plt.title("gender vs height")

plt.subplot(2,3,5)
plt.scatter(df['gender'], df['weight'])
plt.title("gender vs weight")

plt.tight_layout()
plt.show()
