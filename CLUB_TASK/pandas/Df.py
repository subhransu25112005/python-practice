import pandas as pd

# Step 1:) Create a dictionary of data
data = {
    'Name': ['sugu', 'santoor', 'vivek', 'subhankar'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Step 2:) Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Step 3:) Display the DataFrame
print("Original DataFrame:")
print(df)

# Step 4:) Access a specific column
print("\nNames column:")
print(df['Name'])
