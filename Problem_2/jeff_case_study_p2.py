# Initialization code to import necessary libraries
import pandas as pd
import random
import psycopg2
import re
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.style.use('ggplot')
#%matplotlib inline

# Helper function for you to get data from the interview database into a Pandas DataFrame
def get_df(query):
    creds = {
            "user": "interview",
            "password": "i_believe_in_science",
            "host": "ds-psql.a.ki",
            "port": "5432",
            "database": "ds"
             }
    connection_string = "dbname='{db}' port='{port}' user='{user}' password='{password}' host='{host}'"
    connection_string = connection_string.format(host=creds['host'],\
                                                 db=creds['database'],\
                                                 user=creds['user'],\
                                                 port=creds['port'],\
                                                 password=creds['password'])
    connection = psycopg2.connect(connection_string)
    connection.autocommit = True

    cursor = connection.cursor()
    query = re.sub('[\n\t]', ' ', query)
    cursor.execute(query)
    data = cursor.fetchall()
    if data:
        colnames = [desc[0] for desc in cursor.description]
        cursor.close()
        connection.close()
        df = pd.DataFrame(data)
        df.columns = colnames
        return df
    else:
        return None


print ('Querying sales data and calculating unit per price...')
# =============================================================================
# Setup query to obtain info from datastore
# =============================================================================

def massage_data():
    
    QUERY2 = """
        SELECT *
        FROM sales
    """
    
    df1 = get_df(QUERY2)
    
    #Add missing unit price data
    #First obtain unit ID and cost per unit
    non_null_items = """ select * from sales where dollars is not null and units != 0 """
    nn_df = get_df(non_null_items)
    
    #work backwards from existing sales data & unit price data to obtain price per unit
    nn_df['unit_price'] = pd.np.where(nn_df.units == 1, nn_df.dollars, pd.np.where(nn_df.units > 1, (nn_df.dollars / nn_df.units),nn_df.dollars))
    nn_df = nn_df.drop(columns = ['week_ending','store_id','test_control','dollars','units'])
    nn_df = nn_df.drop_duplicates().reset_index()
    
    #create new dataframe with complete inventory of SKUs and prices
    #NOTE - database is missing sales data for item "ACME Thermoscan 3 Ear Thermometer"
    w_df = pd.merge(df1,nn_df, how = 'left', on = 'product_name')
    w_df['sales'] = w_df.units * w_df.unit_price
    
    print (w_df.groupby(['product_name','unit_price']).size().reset_index(name = '# of Items Sold'))
    
    return w_df

massage_data = massage_data()



print ('Looking for location data...')
print ('Joining location data to sales data...')
# =============================================================================
# Join store ID to zipcode in dataset
# =============================================================================
def final_dataframe():
    
    #initialize zipcode query
    zipcode_query = """ select * from retailer_zipcodes """
#    zipcode_income_query = """ select * from zipcode_income"""
    zipcode = get_df(zipcode_query)
    
    #join zipcode df with sales dataframe
    df = pd.merge(massage_data, zipcode, how = 'left', on = 'store_id')
    df = df[df.product_name != 'ACME Thermoscan 3 Ear Thermometer']
    
    return df

working_df = final_dataframe()

print ('Joined location data to sales data.')


print ('Counting number of unique "test" and "controlled" stores...')

# =============================================================================
# Count number of unique control and unique test stores 
# Control - 354 , Test - 13,353, Both - 13,484 
# =============================================================================
def count_distinct_stores():
    
    #initialize query
    count_test = """select count(distinct store_id) from sales where test_control = 'test' """
    test = get_df(count_test)
    
    total_stores = """select count(distinct store_id) from sales """
    total_store_count = get_df(total_stores)
    
    #count number of stores for each control type
    control = int(total_store_count.iloc[0]) - int(test.iloc[0])
    
    print ("Total Number of Stores -",total_store_count.iloc[0] )
    print ("Number of Test Control Stores -", test.iloc[0])
    print ("Number of Control Stores -",control)

store_count = count_distinct_stores()

store_count


print ('Categorizing stores as either "test" or "control"...')
# =============================================================================
# There exists stores labeled as both 'test' and 'control'
# This function finds such stores and labels them as 'test'
# =============================================================================
def categorize_ambiguous_stores(working_df):
    
    #obtain list of stores that have more than one 'test_control' field (e.g. x > 2 )
    both = working_df.copy()
    both = working_df.groupby(['store_id'])['test_control'].nunique().reset_index()
    test_and_control = both[both.test_control == 2]
    test_and_control = test_and_control.drop(columns = ['test_control'])
    test_and_control = test_and_control.drop_duplicates().reset_index()
    #label all of these stores as 'test' variable stores
    test_and_control['test_and_control'] = 'test'
    
    
    #get list of stores with just one label (e.g. 'pure test' stores)
    test_stores = both[both.test_control == 1].reset_index()
    x = test_stores.store_id
    test = working_df[(working_df.test_control == 'test') & (working_df.store_id.isin(x))]
    test['pure_test_label'] = 'test'
    test = test.drop(columns = ['week_ending','product_code_x','product_name','units','dollars','index','product_code_y','unit_price','sales','zipcode','test_control'])
    test = test.drop_duplicates().reset_index()
    
    
    #get list of stores with just one label (e.g. 'pure control' stores)
    control = working_df.copy()
    control = working_df[(working_df.test_control == 'control') & (working_df.store_id.isin(x))]
    control['pure_control_label'] = 'control'
    control = control.drop(columns = ['week_ending','product_code_x','product_name','units','dollars','index','product_code_y','unit_price','sales','zipcode','test_control'])
    control = control.drop_duplicates().reset_index()

    #join the dataframes so each store's 'test_control' field is binary (either only 'test' or 'control')
    df = pd.merge(working_df,test_and_control,how='left',on='store_id')
    df = pd.merge(df,test,how='left',on='store_id')
    df = pd.merge(df,control,how='left',on='store_id')
    df = df.drop(columns = ['product_code_y','index_y','index_x','index_y','index_x'])
    
    return df


final_df = categorize_ambiguous_stores(working_df)




print ('Calculating weekly average sales for "test" and "controlled" stores...')
# =============================================================================
# Calculate weekly average sales for controlled and test stores
# =============================================================================
def weekly_average_sales(final_df):

    #average sales by store by week (control)
    control_stores = final_df[(final_df.pure_control_label == 'control')]
    control = control_stores.groupby(['week_ending'])['sales'].mean().reset_index()
    
    #average sales by store by week (test)
    test_stores = final_df[(final_df.test_and_control == 'test') | (final_df.pure_test_label == 'test')]
    test = test_stores.groupby(['week_ending'])['sales'].mean().reset_index()

    return control, test
    
avg_sale_control, avg_sale_test = weekly_average_sales(final_df)

print ('Weekly average sales (control stores)')
print (avg_sale_control)

print ('Weekly average sales (test stores)')
print (avg_sale_test)



print ('Calculating weekly total sales for "test" and "controlled" stores...')
# =============================================================================
# Calculate weekly total sales for controlled and test stores
# =============================================================================
def total_weekly_sales(final_df):
        
    #total sale by week (control)
    control_stores = final_df[(final_df.pure_control_label == 'control')]    
    control = control_stores.groupby(['week_ending'])['sales'].sum().reset_index()
    
    #total sale by week (test)
    test_stores = final_df[(final_df.test_and_control == 'test') | (final_df.pure_test_label == 'test')]
    test = test_stores.groupby(['week_ending'])['sales'].sum().reset_index()

    return control, test

weekly_sales_control, weekly_sales_test = total_weekly_sales(final_df)


print ('Weekly total sales (control stores)')
print (weekly_sales_control)

print ('Weekly total sales (test stores)')
print (weekly_sales_test)




print ('Measuring lift in sales for "test" stores...')
# =============================================================================
# Measuring lift in sales dollars
# a) Calculate % difference between test and control sale averages 
# b) Take % difference and estimate 'true lift' with existing sales figures
# =============================================================================
def test_control_pct_difference(avg_sale_control, avg_sale_test, weekly_sales_test):
    
    #calculate percent difference for average sale amount (over the 8 weeks) for 'control' and 'test'
    test_control_comparison = pd.merge(avg_sale_control,avg_sale_test,on='week_ending',how='left')
    test_control_comparison.columns = ['week_ending','sale_per_store_control','sale_per_store_test']
    test_control_comparison['pct_difference'] = (test_control_comparison.sale_per_store_test - test_control_comparison.sale_per_store_control)


    #Estimate the revenue difference for the % lift...
    test_revenue_lift = pd.merge(weekly_sales_test,test_control_comparison,on='week_ending',how='left')
    test_revenue_lift['direction'] = (test_revenue_lift.pct_difference >= 0)
    
    #Calculate estimated 'lift' for 'test' stores.
    test_revenue_lift['benchmarked_sales'] = pd.np.where(test_revenue_lift.direction == True,(test_revenue_lift.sales / (1 + (test_revenue_lift.pct_difference/100))), (test_revenue_lift.sales / (1 - (abs(test_revenue_lift.pct_difference/100)))))
    test_revenue_lift['est_lift'] = test_revenue_lift.sales - test_revenue_lift.benchmarked_sales
    
    #return campaign time frame (6 weeks starting 11/18/2018)
    return test_revenue_lift.est_lift[2:].sum()


measure_lift = test_control_pct_difference(avg_sale_control, avg_sale_test, weekly_sales_test)


print ("Lift from campaign is", "$",int(measure_lift), ", which is $", 16000 - int(measure_lift), "short from breaking even on the $16k spend threshold")


if measure_lift < 16000:
    print ("Campaign is NOT worth")
else:
    print ("Campaign is worth")
    



