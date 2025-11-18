# t_test_penguins.py
# Performs an independent samples t-test comparing bill depth between Biscoe and Dream islands.

import pandas as pd
from palmerpenguins import load_penguins
import scipy.stats as stats
from scipy.stats import ttest_ind, levene, shapiro
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.makedirs("results", exist_ok=True)

# Load dataset
penguins = load_penguins()

# Drop missing values
penguins_clean = penguins.dropna(subset=["island", "bill_depth_mm"])

# Filter groups: Biscoe vs Dream
# Filter only Adelie penguins on Biscoe
biscoe = penguins_clean[(penguins_clean["species"] == "Adelie") & (penguins_clean["island"] == "Biscoe")]["bill_depth_mm"]
# Filter only Adelie penguins on Dream
dream = penguins_clean[(penguins_clean["species"] == "Adelie") & (penguins_clean["island"] == "Dream")]["bill_depth_mm"]

# Assumption Checks
print("\n--- Normality Tests (Shapiro-Wilk) ---")
print("Biscoe normality p-value:", shapiro(biscoe).pvalue)
print("Dream normality p-value:", shapiro(dream).pvalue)

print("\n--- Homogeneity of Variance (Levene's Test) ---")
print("Levene p-value:", levene(biscoe, dream).pvalue)

# Independent Samples t-test
t_stat, p_value = ttest_ind(biscoe, dream, equal_var=True)

print("\n--- Independent Samples t-test ---")
print("t-statistic:", t_stat)
print("p-value:", p_value)

print("\n--- Effect Size (Cohen's d) ---")
import numpy as np
import os

# Create results directory\-nos.makedirs("results", exist_ok=True)

mean_diff = np.mean(biscoe) - np.mean(dream)
pool_sd = np.sqrt(((len(biscoe)-1)*np.var(biscoe, ddof=1) + (len(dream)-1)*np.var(dream, ddof=1)) / (len(biscoe)+len(dream)-2))
cohens_d = mean_diff / pool_sd

print("\n--- Effect Size (Cohen's d) ---")
print("Cohen's d:", cohens_d)

# Visualization: Boxplot
plt.figure(figsize=(6,4))
sns.boxplot(data=penguins_clean[penguins_clean["species"]=="Adelie"], x="island", y="bill_depth_mm")
plt.title("Bill Depth (mm) of Adelie Penguins by Island")
plt.tight_layout()
plt.savefig("results/adelie_bill_depth_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

# Visualization: Histograms
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(biscoe, bins=10)
plt.title("Biscoe Bill Depth Distribution")
plt.subplot(1,2,2)
plt.hist(dream, bins=10)
plt.title("Dream Bill Depth Distribution")
plt.tight_layout()
plt.savefig("results/adelie_bill_depth_histograms.png", dpi=300, bbox_inches="tight")
plt.close()

# Q-Q Plots for Normality
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
stats.probplot(biscoe, dist="norm", plot=plt)
plt.title("Q-Q Plot: Biscoe")
plt.subplot(1,2,2)
stats.probplot(dream, dist="norm", plot=plt)
plt.title("Q-Q Plot: Dream")
plt.tight_layout()
plt.savefig("results/adelie_bill_depth_qqplots.png", dpi=300, bbox_inches="tight")
plt.close()

print("\nAnalysis complete. All visualizations saved to the 'results' folder.")