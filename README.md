## Penguins Project

### For EDA check:
```
Penguins
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

### For testing check:
```
Penguins
├── pyproject.toml
├── README.md
├── results
│   ├── adelie_bill_depth_boxplot.png
│   ├── adelie_bill_depth_histograms.png
│   └── adelie_bill_depth_qqplots.png
├── t_test_penguins.py 
└── uv.lock
```

## Clone the repository
`git clone https://github.com/kylezarif/penguins.git`
`cd penguins`

## Setup Instructions
###  Install `uv`
`uv` is a fast Python package and project manager.  
Run the following command in your terminal:

curl -LsSf https://astral.sh/uv/install.sh | sh

`export PATH="$HOME/.local/bin:$PATH"`

### Create and activate the environment using uv
`uv sync`
`source .venv/bin/activate`

### Interpretation of the results
#### Research Question (RQ)
Is there a statistically significant difference in the bill width of chinstrap penguins between Briscoe and Dream Island?

#### Null Hypothesis (H₀)
There is no statistically significant difference in bill width between chinstrap penguins on Briscoe Island and Dream Island.

#### Alternative Hypothesis (H₁)
There is a statistically significant difference in bill width between chinstrap penguins on Briscoe Island and Dream Island.

## Test method: We used an independent two-sample t-test (Welch’s t-test) because:

The data came from two independent groups (Adelie penguins on Biscoe vs Dream Islands).
Normality assumptions were satisfied in both groups.
Variances were not equal, so the unequal-variances version (Welch’s) is the correct test.

## Interpretation of Results in "results folder" 
The analysis shows no meaningful difference in bill depth between Adelie penguins living on Biscoe Island and those on Dream Island.

The normality checks (Shapiro–Wilk) indicate that both groups follow a normal distribution, with p-values of 0.9040 for Biscoe and 0.5184 for Dream.

Levene’s test shows that the two groups also have similar variances (p = 0.5619), meaning the assumptions for running an independent samples t-test were fully met.

The t-test produced a t-statistic of 0.5086 and a p-value of 0.6122, which is far above the usual 0.05 threshold, indicating that the difference in mean bill depth is not statistically significant.

The effect size was very small (Cohen’s d = 0.102), suggesting that even from a biological or practical perspective, the difference between the two island groups is minimal.

The sample sizes were solid—44 Adelie penguins from Biscoe and 56 from Dream—yet the results still showed no meaningful separation between the groups.

Because the statistical evidence does not support a difference, we fail to reject the null hypothesis, meaning Adelie penguins from both islands have similar bill depth measurements.