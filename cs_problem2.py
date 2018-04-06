import pandas as pd
import psycopg2
import re
import matplotlib
import matplotlib.pyplot as plt
import datetime


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


sales_df = get_df("SELECT * FROM sales")

# ##################################### #
# Plotting several charts using pyplot #
# ################################### #
matplotlib.style.use('ggplot')

# CHART 1

sales_df['week_ending'] = pd.to_datetime(sales_df['week_ending'])
week_sls = sales_df.groupby(['week_ending','test_control'])['units'].sum().reset_index(name = 'total_sales')

# Trying to simulate ggplot's color argument for categorical variables

# Method 1 using pandas
week_sls.pivot(index='week_ending', columns='test_control', values='total_sales').plot()
# Method 2 using matplotlib base
week_sls2 = week_sls.pivot(index='week_ending', columns='test_control', values='total_sales').reset_index()
plt.plot(week_sls2.week_ending, week_sls2.test, label='test')
plt.plot(week_sls2.week_ending, week_sls2.control, label='control')
plt.legend()

# CHART 2

# Method 1 using Pandas
week_sls.pivot(index = 'week_ending', columns = 'test_control', values = 'total_sales').plot(subplots = True, sharex = True)
# Method 2 using matplotlib base
fig, axes = plt.subplots(ncols=2, sharex=True)
axes[0].plot(week_sls2.week_ending, week_sls2.test)
axes[0].set_title('Test')
axes[1].plot(week_sls2.week_ending, week_sls2.control, color = 'b')
axes[1].set_title('Control')
for ax in fig.axes:
    matplotlib.pyplot.sca(ax)  # Set the current Axes instance to ax.
    plt.xticks(rotation=90)

# CHART 3

week_sls.columns = ['week_ending','test_control', 'sales']
aux_df = week_sls.copy()
aux_df['week_ending'] += pd.DateOffset(days=7)
aux_df.columns = ['week_ending','test_control', 'prev_sales']
week_sales_growth = week_sls.merge(aux_df, how='left', on=['week_ending','test_control'])
week_sales_growth = week_sales_growth[week_sales_growth['prev_sales'].isna() == False]
week_sales_growth['sales_growth'] = week_sales_growth.eval('(sales - prev_sales)/prev_sales')

# Method 1
week_sales_growth.pivot(index='week_ending', columns='test_control', values='sales_growth').plot()

# Method 2 improved over chart 1, leave index as week_ending and plot only needs 1 argument
# sets x-axis equal to the index
growth_df = week_sales_growth.pivot(index='week_ending', columns='test_control', values='sales_growth')
plt.plot(growth_df.test, label='test')
plt.plot(growth_df.control, label='control')
plt.xticks(rotation=90)
plt.legend()

# Redoing the panda's chart output using matplotlib base
import matplotlib.dates as mdates
fig, ax = plt.subplots()
ax.plot(growth_df.test, label='test')
ax.plot(growth_df.control, label='control')
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.xticks(rotation=45)
plt.legend(title='test_control')


# ############################### #
# Solving the Sales Lift Problem  #
# ############################### #
week_sales = sales_df.groupby(['week_ending','test_control','store_id'])['units'].sum().reset_index()

start_exp_dt = datetime.date(2017, 11, 12)
ctrl_prior_exp_df = week_sales[(week_sales['week_ending'] < start_exp_dt) & (week_sales['test_control'] == 'control')]
ctrl_prior_exp_df = ctrl_prior_exp_df.groupby(['store_id'])['units'].mean()
ctrl_after_exp_df = week_sales[(week_sales['week_ending'] >= start_exp_dt) & (week_sales['test_control'] == 'control')]
ctrl_after_exp_df = ctrl_after_exp_df.groupby(['store_id'])['units'].mean()
ctrl_df = pd.concat([ctrl_prior_exp_df, ctrl_after_exp_df], axis=1)
ctrl_df.columns = ['sales_before', 'sales_after']
ctrl_df['diff'] = ctrl_df.eval('sales_after - sales_before')

test_prior_exp_df = week_sales[(week_sales['week_ending'] < start_exp_dt) & (week_sales['test_control'] == 'test')]
test_prior_exp_df = test_prior_exp_df.groupby(['store_id'])['units'].mean()
test_after_exp_df = week_sales[(week_sales['week_ending'] >= start_exp_dt) & (week_sales['test_control'] == 'test')]
test_after_exp_df = test_after_exp_df.groupby(['store_id'])['units'].mean()
test_df = pd.concat([test_prior_exp_df, test_after_exp_df], axis=1)
test_df.columns = ['sales_before', 'sales_after']
test_df['diff'] = test_df.eval('sales_after - sales_before')

mean_0 = ctrl_df['diff'].mean()
sd_0 = ctrl_df['diff'].std()
n_0 = len(ctrl_df.index)

mean_1 = test_df['diff'].mean()
sd_1 = test_df['diff'].std()
n_1 = len(test_df.index)

t0 = mean_0/(sd_0/n_0**0.5)
t1 = mean_1/(sd_1/n_1**0.5)

print('t0 is greater than 1.6: ' + str(t0 > 1.6))
print('t1 is greater than 1.6: ' + str(t1 > 1.6))
