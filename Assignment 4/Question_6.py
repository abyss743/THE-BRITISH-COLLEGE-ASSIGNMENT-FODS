'''
This program adds BMI and Health_Status columns to health_data.csv
'''

import pandas as pd

df = pd.read_csv("health_data.csv")

df['BMI'] = df['weight'] / ((df['height']/100)**2)

def get_status(b):
    if b < 18.5: return "Underweight"
    elif b <= 24.9: return "Healthy range"
    elif b <= 29.9: return "Overweight risk"
    elif b <= 34.9: return "High risk of diabetes/heart disease"
    else: return "Critical health condition"

df['Health_Status'] = df['BMI'].apply(get_status)

print(df[['weight','height','BMI','Health_Status']])
df.to_csv("health_updated.csv", index=False)
