#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:38:53 2018

@author: patricio
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from lib import cs_utilities as utl
style.use('ggplot')

income_df = utl.get_df("SELECT * FROM zipcode_income")

# Setting income_band as categorical variable
bands = income_df['income_band'].unique()
income_df['income_band'] = income_df.income_band.astype('category',
                                                        categories=bands, ordered=True)

# Building table with the median income

income_df = income_df.sort_values(['state', 'zipcode', 'income_band'])
income_df = income_df.drop(['total_income_millions'], axis=1)
income_df['cum_freq'] = income_df.groupby(['state', 'zipcode'])['num_households'].cumsum()

income_df['prev_cum_freq'] = income_df.cum_freq.shift()
income_df['prev_cum_freq'][(income_df['income_band'] == '<$25k')] = 0

households_df = income_df.groupby(['state', 'zipcode'])['num_households'].sum().reset_index()

households_df['adj_num_households'] = households_df['num_households'].copy()
households_df['adj_num_households'][(households_df['adj_num_households'] % 2 == 1)] += 1

households_df['half_tot_households'] = households_df['adj_num_households'] // 2
households_df = households_df.drop(['num_households', 'adj_num_households'], axis=1)

bins_range = [25000, 25000, 25000, 25000, 100000, np.nan]
lower_end = [0, 25000, 50000, 75000, 100000, 200000]

aux_df = pd.DataFrame({'income_band': bands, 'bins_range': bins_range,
                       'lower_end': lower_end})

income_df = income_df.merge(households_df, how='left', on=['state', 'zipcode'])
income_df['ind_median_bin'] = (income_df['half_tot_households'] > income_df['prev_cum_freq']) & \
                              (income_df['half_tot_households'] <= income_df['cum_freq'])

median_df = income_df[(income_df['ind_median_bin'] == True)]
median_df = median_df.merge(aux_df, how='left', on='income_band')
median_df['median_value'] = median_df.eval('lower_end\
         + (half_tot_households-prev_cum_freq)/num_households*bins_range')
wanted_cols = ['state', 'zipcode', 'median_value']
median_df = median_df[wanted_cols]

store_df = utl.get_df("""SELECT * FROM retailer_zipcodes
                     WHERE zipcode not in ('00000','99999')""")

# There are supposedly 11 weeks of sales registries in the sales table
# This query help us to determine if for every store there are 11 weeks of
# information.

valid_df = utl.get_df('''SELECT store_id, COUNT(*) as cuenta
                     FROM(
                     SELECT DISTINCT store_id, week_ending
                     FROM sales) as A
                     GROUP BY store_id
                     HAVING COUNT(*) <> 11''')
print(len(valid_df))

# There are 3393 stores that only have 10 weeks of information
# Since we don't actually know what happened and it's a strong assumption
# to suppose that they sold 0 during the missing week, we will use the average
# weekly sales to measure the effect of median income in sales

sales_df = utl.get_df('''SELECT store_id, AVG(units_sold) as avg_sales
                     FROM(
                         SELECT store_id, week_ending, SUM(units) as units_sold
                         FROM sales
                         GROUP BY store_id, week_ending
                         ) AS sls
                     GROUP BY store_id''')

store_df = store_df.merge(sales_df, how='left', on=['store_id'])
store_df = store_df.merge(median_df, how='left', on=['zipcode'])

store_df['avg_sales'] = pd.to_numeric(store_df['avg_sales'])
store_df.plot.scatter('median_value', 'avg_sales', figsize=(8, 5))
store_df['avg_sales'].corr(store_df['median_value'], method='pearson')

# So it seems that there's no relation between income and termometer sales
# but to go further we will check later if there are states in which termometer
# sales are higher.

#####################
# Regression Model #
####################

# Build a regression only with the median_income
lin_mod = ols(formula="avg_sales ~ median_value",
              data=store_df).fit()

print(lin_mod.summary())
# p-value approx 0.

results = pd.DataFrame({'store_id': store_df.store_id,
                        'resids': lin_mod.resid,
                        'std_resids': lin_mod.resid_pearson,
                        'fitted': lin_mod.predict()})

## Diagnostic plots

# plt.style.use('seaborn')
# plt.rc('font', size=14)
# plt.rc('figure', titlesize=18)
# plt.rc('axes', labelsize=15)
# plt.rc('axes', titlesize=18)

# Residuals vs Fitted
plt.scatter(results['fitted'], results['resids'], color='b')
plt.axhline(y=0, color='grey', linestyle='dashed')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted')
plt.show()

# Normal Q-Q
qqplot = sm.qqplot(results['std_resids'], line='s')
plt.show(qqplot)

# Scale-Location (homoscedasticity, i.e equal variance)
scalelocplot = plt.plot(results['fitted'], abs(results['std_resids']) ** .5, 'o',
                        color='b')
plt.xlabel('Fitted values')
plt.ylabel('Square Root of |standardized residuals|')
plt.title('Scale-Location')
plt.show(scalelocplot)

# Residuals vs Leverage
residsvlevplot = sm.graphics.influence_plot(lin_mod, criterion='Cooks',
                                            size=2)
plt.show(residsvlevplot)

## 4 plots in one window

utl.plot_linear_model(lin_mod)

# We will now verify if there are any states in which sales are significantly
# higher.

state_df = store_df.groupby('state')['avg_sales'].mean()
store_df.groupby('state')['avg_sales'].mean().plot.bar(figsize=(12, 8))
# store_df.boxplot('avg_sales', by = 'state', figsize = (12, 8))

# From the plot we can be confident that there's difference on average sales
# per store between states but we can run conduct a one-way ANOVA analysis

import statsmodels.api as sm
from statsmodels.formula.api import ols

mod = ols('avg_sales ~ state', data=store_df).fit()

aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)

# We can conclude that there's at least 1 state for whom the average sales
# per store is higher when compared with other states.
# My best guess is that states in which sales are higher are the ones that
# experience the most extreme temperatures (leaning towards lower temperatures)

''' Dummy Variables

state_df = state_df.sort_values(ascending=False)
 wanted_states = state_df.index[0:5]

store_df['top_sales_st'] = store_df['state']
# We simulate 'not in' expression by putting ~ at the beginning of the filter
store_df['top_sales_st'][(~store_df['top_sales_st'].isin(wanted_states))] = 'Others'
# Create dummy variables
dummies = pd.get_dummies(store_df['state'])

store_df = pd.concat([store_df, dummies], axis=1)

'''

# Applying KS Statistic to see differences in sales distribution between states

dist1 = store_df['avg_sales'][store_df['state'] == 'NY']
dist2 = store_df['avg_sales'][store_df['state'] == 'NJ']


utl.plot_KS_stat(dist1, dist2)
utl.ks_test_2samp(dist1, dist2, 0.01)