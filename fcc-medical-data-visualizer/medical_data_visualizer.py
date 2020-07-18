import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['height_m'] = df['height'].apply(lambda x: x/100)
df['height_m'] = df['height_m'].apply(lambda x: x**2)
df['BMI'] = df['weight'] / df['height_m']
df['overweight'] = np.where((df['BMI'] > 25), 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where((df['cholesterol'] == 1), 0, 1)
df['gluc'] = np.where((df['gluc'] == 1), 0, 1)

# Draw Categorical Plot
cat_cols = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=cat_cols)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable']).agg({'value':'value_counts'})
    df_cat.columns = ['total']
    df_cat.reset_index(inplace=True)

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, col='cardio', x='variable', y='total', hue='value', kind='bar', height=7);
    fig = plt.gcf()

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
df.drop(columns=['height_m', 'BMI'], inplace=True)
def draw_heat_map():
    # Clean the data

    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(13,8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f', vmax=0.3, center=0, square=False, linewidths=0.5, cbar_kws={'shrink':0.5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig