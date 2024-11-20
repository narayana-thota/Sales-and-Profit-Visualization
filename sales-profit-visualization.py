
import pandas as pd
import matplotlib.pyplot as plt

# Create or load a Pandas DataFrame
# Example DataFrame (replace this with your actual data)
data = {
    'Year': [2010, 2011, 2012, 2013, 2014],
    'Sales': [100, 150, 200, 180, 220],
    'Profit': [20, 25, 30, 28, 35]
}
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Year'], df['Sales'], color='blue', label='Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Over Years')
plt.legend()
plt.grid(True)

# Show the bar chart
plt.show()

# Create a line chart
plt.figure(figsize=(8, 6))
plt.plot(df['Year'], df['Profit'], marker='o', color='green', label='Profit')
plt.xlabel('Year')
plt.ylabel('Profit')
plt.title('Profit Over Years')
plt.legend()
plt.grid(True)

# Show the line chart
plt.show()


 