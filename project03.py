# ==============================
# IMPORT LIBRARIES
# ==============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn style
sns.set()

# ==============================
# NUMPY (Numerical Operations)
# ==============================
print("----- NUMPY -----")

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

arr2 = np.arange(1, 10).reshape(3, 3)
print("2D Array:\n", arr2)

# ==============================
# PANDAS (Data Handling)
# ==============================
print("\n----- PANDAS -----")

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

print("\nDescribe:\n", df.describe())

# ==============================
# SEABORN VISUALIZATION
# ==============================
print("\n----- SEABORN -----")

# Line Plot
plt.figure()
sns.lineplot(x="Name", y="Marks", data=df)
plt.title("Marks Line Chart")
plt.show()

# Bar Plot
plt.figure()
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Marks Bar Chart")
plt.show()

# Scatter Plot
plt.figure()
sns.scatterplot(x="Age", y="Marks", data=df)
plt.title("Age vs Marks")
plt.show()

# Histogram
plt.figure()
sns.histplot(df["Marks"], kde=True)
plt.title("Marks Distribution")
plt.show()

# Box Plot
plt.figure()
sns.boxplot(x="Marks", data=df)
plt.title("Box Plot of Marks")
plt.show()

# ==============================
# HEATMAP (Correlation)
# ==============================
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()