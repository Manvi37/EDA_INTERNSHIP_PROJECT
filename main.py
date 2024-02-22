import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("venv/used_cars_data.csv", delimiter='\t')

# Display summary statistics of the dataset
print(df.describe())

# Check the data types of columns
print(df.dtypes)

# Debugging: Print out the columns of the DataFrame
print(df.columns)

# Drop unnecessary columns and rename some columns for clarity
if 'New_Price' in df.columns:
    df.drop(['New_Price'], axis=1, inplace=True)
df.rename(columns={"Kilometers_Driven": "Kilometers", "Fuel_Type": "FuelType", "Owner_Type": "Owner"}, inplace=True)

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Drop rows with missing values
df.dropna(inplace=True)

# Additional functionality: Convert 'Price' to numeric
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Visualize the distribution of Price
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, bins=20, color='skyblue')
plt.title('Distribution of Car Prices')
plt.xlabel('Price (in Lakhs)')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between Mileage and Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mileage', y='Price', data=df, hue='Owner')
plt.title('Mileage vs. Price')
plt.xlabel('Mileage')
plt.ylabel('Price (in Lakhs)')
plt.legend(title='Owner')
plt.show()

# Visualize the counts of different Fuel Types
plt.figure(figsize=(8, 5))
sns.countplot(x='FuelType', data=df, palette='Set2')
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()

# Visualize the correlation matrix with a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Additional functionality: Convert 'Price' to numeric
if 'Price' in df.columns:
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
else:
    print("The 'Price' column does not exist in the dataset.")

# Print out the column names with special characters escaped
print(df.columns.tolist())

# Load the first few rows of the CSV file to inspect the delimiter
with open("venv/used_cars_data.csv", "r") as file:
    for _ in range(5):
        print(file.readline())
