#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:06:51 2018

@author: jeff
"""

# Initialization code to import necessary libraries
import pandas as pd
import psycopg2
import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

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


# =============================================================================
# Problem 1 - finding median income bins
# =============================================================================

def find_median_income_bands():
    
    SAMPLE_QUERY = """
        SELECT *
        FROM zipcode_income
        where zipcode is not null and num_households is not null and total_income_millions is not null
        ;
    """
    
    df = get_df(SAMPLE_QUERY)
    df = df.drop(columns = ['total_income_millions'])
    
    
    #find median of aggregated values based on state & zipcode combo
    median_df = df.groupby(['state','zipcode'])['num_households'].sum().reset_index()
    median_df['median_values'] = (median_df.num_households/2)
    
    #create a new column to find cumulative sum, this will be used to determine income_band bins
    df['households_cumulative'] = df.groupby(['state','zipcode'])['num_households'].cumsum()
    
    #shift the column down one position to create 'bin ranges'
    df['shifted_cumulative'] = df.households_cumulative.shift(1)
    
    #merge the household medians with the main dataframe
    working_df = pd.merge(df, median_df, how = 'left', on = ['state','zipcode'])
    
    #median income band is determined by bins. (e.g. return all rows where the median income is between two bin ranges in that row)
    working_df['median_income'] = ((working_df.median_values > working_df.shifted_cumulative) & (working_df.median_values <= working_df.households_cumulative))
    median_incomes = working_df[working_df.median_income == True]
    
    return median_incomes

median_incomes = find_median_income_bands()

print (median_incomes.head(10))






