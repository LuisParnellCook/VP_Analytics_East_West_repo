import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os

os.makedirs('Data', exist_ok=True)

# Load panel
panel_path = 'Data/earnings_regression_panel.csv'
print('Loading', panel_path)
df = pd.read_csv(panel_path, parse_dates=['Earnings Date'])
print('panel shape:', df.shape)

# Normalize column names
if 'Δ10Y' in df.columns and 'D10Y' not in df.columns:
    df = df.rename(columns={'Δ10Y':'D10Y'})

# Ensure numeric
for c in ['Surprise','CAR','VIX','D10Y']:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')

# Drop missing key
df = df.dropna(subset=['Surprise','CAR'])
print('After dropping NA key vars:', df.shape)

# Means by Regime
if 'Regime' in df.columns:
    means = df.groupby('Regime')[['Surprise','CAR']].mean()
    print('\nMeans by Regime:\n', means)
    means.to_csv('Data/means_by_regime.csv')
else:
    print('No Regime column found')

sns.set(style='whitegrid')

# Boxplots
if 'Regime' in df.columns:
    plt.figure(figsize=(8,6))
    sns.boxplot(x='Regime', y='Surprise', data=df)
    plt.title('Surprise by Regime')
    plt.tight_layout()
    plt.savefig('Data/fig_surprise_box.png')

    plt.figure(figsize=(8,6))
    sns.boxplot(x='Regime', y='CAR', data=df)
    plt.title('CAR by Regime')
    plt.tight_layout()
    plt.savefig('Data/fig_car_box.png')

# Scatter
plt.figure(figsize=(8,6))
if 'Regime' in df.columns:
    sns.scatterplot(x='Surprise', y='CAR', hue='Regime', data=df, alpha=0.8)
else:
    sns.scatterplot(x='Surprise', y='CAR', data=df, alpha=0.8)
plt.title('Surprise vs CAR')
plt.tight_layout()
plt.savefig('Data/fig_scatter.png')

# Regression
terms = ['Surprise']
if 'Regime' in df.columns:
    terms.append('C(Regime)')
if 'VIX' in df.columns:
    terms.append('VIX')
if 'D10Y' in df.columns:
    terms.append('D10Y')

formula = 'CAR ~ ' + ' + '.join(terms)
print('\nFormula:', formula)

model = smf.ols(formula=formula, data=df).fit()
print(model.summary())

with open('Data/regression_summary.txt', 'w') as f:
    f.write(str(model.summary()))

print('\nSaved plots: Data/fig_surprise_box.png, Data/fig_car_box.png, Data/fig_scatter.png')
print('Saved regression summary to Data/regression_summary.txt')
print('Saved means to Data/means_by_regime.csv (if computed)')
