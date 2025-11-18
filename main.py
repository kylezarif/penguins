# eda_penguins.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins

# Load the dataset
penguins = load_penguins()

# --- Basic Info ---
print("\n🔹 First 5 rows:")
print(penguins.head())

print("\n🔹 Dataset Info:")
print(penguins.info())

print("\n🔹 Missing values:")
print(penguins.isnull().sum())

# --- Basic Statistics ---
print("\n🔹 Summary statistics:")
print(penguins.describe())

# --- Drop missing values for plotting ---
penguins_clean = penguins.dropna()

# --- Visualizations ---
sns.set(style="whitegrid", palette="muted")

# 1. Species distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=penguins_clean, x="species", hue="sex")
plt.title("Species Count by Sex")
plt.tight_layout()
plt.show()

# 2. Pairplot for numerical features
sns.pairplot(penguins_clean, hue="species")
plt.suptitle("Pairplot of Penguin Features", y=1.02)
plt.show()

# 3. Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(
    penguins_clean.corr(numeric_only=True),
    annot=True, cmap="coolwarm", linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 4. Body mass by species
plt.figure(figsize=(6, 4))
sns.boxplot(data=penguins_clean, x="species", y="body_mass_g", hue="sex")
plt.title("Body Mass by Species and Sex")
plt.tight_layout()
plt.show()

# 5. Bill depth by island (your variable of interest)
plt.figure(figsize=(6, 4))
sns.boxplot(data=penguins_clean, x="island", y="bill_depth_mm")
plt.title("Bill Depth (mm) by Island")
plt.tight_layout()
plt.show()

print("\n EDA complete!")
