import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('C:\WebDev\PYTHON\FreeCodeCamp Data Analysis\Medical Data Visualizer\medical_examination.csv')

# 2
# Calculate BMI
df['height'] = df['height'] / 100
df['BMI'] = df['weight'] / df['height'] ** 2
df['BMI'] = round(df['BMI'], 1)

# Add overweight column
df['overweight'] = 0
df.loc[df['BMI'] > 25, 'overweight'] = 1

# 3
# Normalize cholesterol and gluc columns. 0 always good, 1 always bad. If value is 1, make 0. If greater than 1, make 1.
df[['cholesterol', 'gluc']] = np.where(df[['cholesterol', 'gluc']] == 1, 0, 1)

# Clean df
height_quantile_low = df['height'].quantile(0.025)
height_quantile_high = df['height'].quantile(0.975)
weight_quantile_low = df['weight'].quantile(0.025)
weight_quantile_high = df['weight'].quantile(0.975)

df = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= height_quantile_low) &
        (df['height'] <= height_quantile_high) &
        (df['weight'] >= weight_quantile_low) &
        (df['weight'] <= weight_quantile_high)]

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6

    # 7

    # 8
    sns.set_theme(style='whitegrid')
    fig = sns.catplot(df_cat, x='variable', kind='count', hue='value', col='cardio')
    fig.set_axis_labels('variable', 'total')


    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    plt.figure(figsize=(10,5))
    fig = sns.heatmap(corr, annot=True, fmt=".1f",  mask=mask)

    # 16
    fig.savefig('heatmap.png')
    return fig
