# t_test_penguins.py
# Performs an independent samples t-test comparing bill depth between
# Adelie penguins on Biscoe Island vs Dream Island.

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import ttest_ind, levene, shapiro
from palmerpenguins import load_penguins

# Ensure results directory exists
os.makedirs("results", exist_ok=True)

# Load dataset
penguins = load_penguins()

# Drop missing values
penguins_clean = penguins.dropna(subset=["island", "bill_depth_mm"])

# Filter Adelie penguins on Biscoe
biscoe = penguins_clean[
    (penguins_clean["species"] == "Adelie") &
    (penguins_clean["island"] == "Biscoe")
]["bill_depth_mm"]

# Filter Adelie penguins on Dream
dream = penguins_clean[
    (penguins_clean["species"] == "Adelie") &
    (penguins_clean["island"] == "Dream")
]["bill_depth_mm"]

# Statistical Tests

print("\nNormality Tests (Shapiro-Wilk)")
biscoe_norm = shapiro(biscoe).pvalue
dream_norm = shapiro(dream).pvalue
print("Biscoe normality p-value:", biscoe_norm)
print("Dream normality p-value:", dream_norm)

print("\nHomogeneity of Variance (Levene's Test)")
levene_p = levene(biscoe, dream).pvalue
print("Levene p-value:", levene_p)

print("\nIndependent Samples t-test")
t_stat, p_value = ttest_ind(biscoe, dream, equal_var=True)
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Effect Size

mean_diff = np.mean(biscoe) - np.mean(dream)
pool_sd = np.sqrt(
    ((len(biscoe) - 1) * np.var(biscoe, ddof=1) +
     (len(dream) - 1) * np.var(dream, ddof=1))
    / (len(biscoe) + len(dream) - 2)
)
cohens_d = mean_diff / pool_sd

print("\nEffect Size (Cohen's d)")
print("Cohen's d:", cohens_d)

# Save Results to Text File

results_text = f"""
Normality Tests (Shapiro-Wilk)
Biscoe normality p-value: {biscoe_norm}
Dream normality p-value: {dream_norm}

Homogeneity of Variance (Levene's Test)
Levene p-value: {levene_p}

Independent Samples t-test
t-statistic: {t_stat}
p-value: {p_value}

Effect Size (Cohen's d)
Cohen's d: {cohens_d}

Sample Sizes
Adelie penguins on Biscoe: {len(biscoe)}
Adelie penguins on Dream: {len(dream)}
"""

with open("results/results.txt", "w") as f:
    f.write(results_text)

print("\nStatistical results saved to results/results.txt")

# Visualizations 

# Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(
    data=penguins_clean[penguins_clean["species"] == "Adelie"],
    x="island",
    y="bill_depth_mm"
)
plt.title("Bill Depth (mm) of Adelie Penguins by Island")
plt.tight_layout()
plt.savefig("results/adelie_bill_depth_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

# Histograms
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(biscoe, bins=10)
plt.title("Biscoe Bill Depth Distribution")
plt.subplot(1, 2, 2)
plt.hist(dream, bins=10)
plt.title("Dream Bill Depth Distribution")
plt.tight_layout()
plt.savefig("results/adelie_bill_depth_histograms.png", dpi=300, bbox_inches="tight")
plt.close()

# Q-Q Plots
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
stats.probplot(biscoe, dist="norm", plot=plt)
plt.title("Q-Q Plot: Biscoe")
plt.subplot(1, 2, 2)
stats.probplot(dream, dist="norm", plot=plt)
plt.title("Q-Q Plot: Dream")
plt.tight_layout()
plt.savefig("results/adelie_bill_depth_qqplots.png", dpi=300, bbox_inches="tight")
plt.close()

print("\nAnalysis complete. All visualizations saved to the 'results' folder.")
