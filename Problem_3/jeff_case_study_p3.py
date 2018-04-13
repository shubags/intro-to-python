#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:34:47 2018

@author: jeff
"""

# Initialization code to import necessary libraries
import pandas as pd
import os


os.chdir("/Users/jeff/Documents/python/case_study")

from jeff_case_study_p1 import median_incomes
from jeff_case_study_p2 import final_df


print ('Calculating sales by location (zipcode)...')
# =============================================================================
# next step is to measure lift or sales by zipcode
# also need to consider outliers (look at test/control stores with 0 sales)
# =============================================================================
def zipcodes_no_sales(final_df):

    control_stores = final_df[(final_df.pure_control_label == 'control')]
    control = control_stores.groupby(['week_ending','zipcode'])['sales'].sum().reset_index()
    
    test_stores = final_df[(final_df.test_and_control == 'test') | (final_df.pure_test_label == 'test')]
    test = test_stores.groupby(['week_ending','zipcode'])['sales'].sum().reset_index()
    
    control_pct = ((control[control.sales == 0].count()) - (control[control.sales != 0].count())) /(control.sales.count())
    test_pct = ((test[test.sales == 0].count()) - (test[test.sales != 0].count())) /(test.sales.count())

    zipcode_list_test = test.zipcode
    zipcode_list_control = control.zipcode

    return control, test, control_pct[0], test_pct[0], zipcode_list_test, zipcode_list_control

zip_sales_control, zip_sales_test, control_pct, test_pct, zipcode_list_test, zipcode_list_control = zipcodes_no_sales(final_df)

print ("Percent of 'control' stores with 0 sales over the testing period -", control_pct)
print ("Percent of 'test' stores with 0 sales over the testing period -", test_pct)


# =============================================================================
# Count how many stores did not sell anything at all as a 
# percentage of total stores for each test_control type
# =============================================================================
def underperforming_zipcodes(control, test):
    
    control_zip = control.groupby(['week_ending','sales'])['zipcode'].count()/(control.zipcode.nunique())
    test_zip = test.groupby(['week_ending','sales'])['zipcode'].count()/(test.zipcode.nunique())
    
    return control_zip, test_zip

under_control, under_test = underperforming_zipcodes(zip_sales_control, zip_sales_test)



# =============================================================================
# now let's go into sales by zipcode location
# =============================================================================
def sales_by_zipcode(df):
    
    #sum all sales by zipcode using final_df from Problem 2
    zipcode_total_sale = df.groupby(['zipcode'])['sales'].sum().reset_index()
    
    #join zipcode sales data from Problem 2 and median_income data from Problem 1
    sales_and_hhi = pd.merge(zipcode_total_sale, median_incomes,on='zipcode',how='left' )
    
    #sum sales by income band
    avg_sale_band = sales_and_hhi.groupby(['income_band'])['sales'].sum().reset_index()
    avg_sale_band['pct_of_total'] = (avg_sale_band.sales / avg_sale_band.sales.sum())
    
    return avg_sale_band.sort_values('pct_of_total',ascending=False), sales_and_hhi

sales_by_zipcode, sales_and_hhi = sales_by_zipcode(final_df)

print ("Percentage of total sales categorized by income band")
print (sales_by_zipcode)



def top_sales_by_location(zip_sales_test, sales_and_hhi):
    df = pd.merge(zip_sales_test, sales_and_hhi, how = 'left', on = 'zipcode')
    df1 = df.groupby(['zipcode','income_band'])['sales_y'].sum().reset_index().sort_values('sales_y',ascending = False)
    df1['pct_of_sales_sum'] = df1.sales_y/(df1.sales_y.sum())*100
    #find high performing zipcodes (top 10%) and low performing zipcodes (bottom 10%)
    return df1.head(50)
    

print ("Percentage of all sales by zipcode and income band")
print (top_sales_by_location(zip_sales_test, sales_and_hhi))

print ("Based on the analysis above, higher income does not translate into greater sales figures")






