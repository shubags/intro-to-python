import pandas as pd
import numpy as np
import psycopg2
import re
import matplotlib

matplotlib.style.use('ggplot')


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
    
    
income_df = get_df("SELECT * FROM zipcode_income")

# Setting income_band as catagorical variable
bands = income_df['income_band'].unique()
income_df['income_band'] = income_df.income_band.astype('category', categories=bands, ordered=True)

##################
#### Plotting ###
#################

plot_df = income_df[(income_df['state'] == 'AK') & (income_df['zipcode'] == '00000')].copy()
plot_df['cum_freq'] = plot_df['num_households'].cumsum()
plot_df['rel_cum_freq'] = plot_df['cum_freq']/plot_df['num_households'].sum()

# Building the plot and set labels for x-axis
graph = plot_df.plot(x='income_band', y='rel_cum_freq')
graph.axes.set_xticklabels(bands)
# vertical lines
graph.axvline(0, color='b', linestyle='--')
graph.axvline(1, color='b', linestyle='--')
# horizontal lines
graph.axhline(plot_df['rel_cum_freq'][(plot_df['income_band'] == '<$25k')].values, color='b', linestyle='--')
graph.axhline(plot_df['rel_cum_freq'][(plot_df['income_band'] == '$25k-$50k')].values, color='b', linestyle='--')
# labels and title
graph.set_xlabel("Income Band")
graph.set_ylabel("Cumulative Frequency")
graph.set_title("Income Study")


#################################
#### Solving for the median #####
#################################

income_df = income_df.sort_values(['state','zipcode','income_band'])
income_df = income_df.drop(['total_income_millions'], axis=1)

# Computing cummulative frequency
income_df['cum_freq'] = income_df.groupby(['state','zipcode'])['num_households'].cumsum()

# Creating the lagged column (shift method)
income_df['prev_cum_freq'] = income_df.cum_freq.shift()
income_df['prev_cum_freq'][(income_df['income_band'] == '<$25k')] = np.nan

# Finding number of households for each state,zip_code
households_df = income_df.groupby(['state','zipcode'])['num_households'].sum().reset_index()

# We add 1 if the total number of households is even
households_df['adj_num_households'] = households_df['num_households'].copy()
households_df['adj_num_households'][(households_df['adj_num_households'] % 2 == 1)] += 1

# We compute half_tot_households (equivalent to n/2 in formula for the median)
households_df['half_tot_households'] = households_df['adj_num_households']//2
households_df = households_df.drop(['num_households','adj_num_households'], axis=1)

bins_range = [25000,25000,25000,25000,100000,np.nan]
lower_end = [0,25000,50000,75000,100000,200000]

aux_df = pd.DataFrame({'income_band': bands, 'bins_range': bins_range, 
                       'lower_end': lower_end})

# Merging all the new dataframes in order to get the data to compute the medians
income_df = income_df.merge(households_df, how = 'left', on = ['state', 'zipcode'])
income_df['ind_median_bin'] = (income_df['half_tot_households'] > income_df['prev_cum_freq']) & \
                              (income_df['half_tot_households'] < income_df['cum_freq'])
median_df = income_df[(income_df['ind_median_bin'] == True)]


# CHECKING THERE IS ONLY A MEDIAN GROUP FOR EVERY STATE,ZIPCODE
check_df = median_df[['state', 'zipcode']]
check_df = check_df.groupby(['state','zipcode']).size().reset_index(name='cuenta')
len(check_df[check_df['cuenta']>1])

median_df = median_df.merge(aux_df, how='left', on='income_band')

# Applying formula for the median, eval method similar to attach dataset
median_df['median_value'] = median_df.eval('lower_end + (half_tot_households-prev_cum_freq)/num_households*bins_range')
print(median_df[['state','zipcode','income_band','median_value']].head(10))

# Sates, zipcodes without median
# median_df[(median_df['median_value'].isna())]

