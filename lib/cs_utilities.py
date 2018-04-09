import psycopg2
import pandas as pd
import re
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math


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


def plot_linear_model(lin_mod):
    results = pd.DataFrame({'resids': lin_mod.resid,
                            'std_resids': lin_mod.resid_pearson,
                            'fitted': lin_mod.predict()})
    fig = plt.figure(figsize=(8, 8), dpi=100)
    ax1 = fig.add_subplot(2, 2, 1)  # 2 by 2 grid and we set first subplot in (-, +)

    ax1.plot(results['fitted'], results['resids'], 'o')
    plt.axhline(y=0, color='grey', linestyle='dashed')
    ax1.set_xlabel('Fitted values')
    ax1.set_ylabel('Residuals')
    ax1.set_title('Residuals vs Fitted')

    ax2 = fig.add_subplot(2, 2, 2)  # (+, +)
    sm.qqplot(results['std_resids'], line='s', ax=ax2)
    ax2.set_title('Normal Q-Q')

    ax3 = fig.add_subplot(2, 2, 3)  # (-, -)
    ax3.plot(results['fitted'], abs(results['std_resids']) ** .5, 'o')
    ax3.set_xlabel('Fitted values')
    ax3.set_ylabel('Sqrt(|standardized residuals|)')
    ax3.set_title('Scale-Location')

    ax4 = fig.add_subplot(2, 2, 4)  # (+, -)
    sm.graphics.influence_plot(lin_mod, criterion='Cooks', size=2, ax=ax4)
    plt.tight_layout()
    return plt.show()


def plot_KS_stat(dist1, dist2):
    dist1 = pd.DataFrame(dist1.value_counts()).sort_index()
    dist1.columns = ['cuenta']
    n1 = dist1['cuenta'].sum()
    dist1['empirical_distr'] = dist1['cuenta'].cumsum()/n1


    dist2 = pd.DataFrame(dist2.value_counts()).sort_index()
    dist2.columns = ['cuenta']
    n2 = dist2['cuenta'].sum()
    dist2['empirical_distr'] = dist2['cuenta'].cumsum()/n2

    ks_df = dist1.join(dist2, how='outer', lsuffix='_1', rsuffix='_2')
    ks_df = ks_df.fillna(method='ffill')
    ks_df['distr_diff'] = ks_df.eval('empirical_distr_1 - empirical_distr_2')
    ks_df['distr_diff'] = ks_df['distr_diff'].abs()
    KS_Statistic = max(ks_df['distr_diff'])
    ks_info = ks_df[(ks_df['distr_diff'] == KS_Statistic)]

    plt.step(dist1.index, dist1['empirical_distr'], color='r', label='Cumulattive Distribution 1')
    plt.step(dist2.index, dist2['empirical_distr'], color='b', label='Cumulattive Distribution 2')
    plt.axvline(x=ks_info.index, color='grey', linestyle='dashed')
    plt.axhline(y=ks_info.empirical_distr_1.values, color='grey', linestyle='dashed')
    plt.axhline(y=ks_info.empirical_distr_2.values, color='grey', linestyle='dashed')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Cumulative Probability')
    plt.title('KS Statistic = ' + str(round(KS_Statistic, 3)))


def ks_test_2samp(dist1, dist2, significance_level):
    dist1 = pd.DataFrame(dist1.value_counts()).sort_index()
    dist1.columns = ['cuenta']
    n1 = dist1['cuenta'].sum()
    dist1['empirical_distr'] = dist1['cuenta'].cumsum()/n1


    dist2 = pd.DataFrame(dist2.value_counts()).sort_index()
    dist2.columns = ['cuenta']
    n2 = dist2['cuenta'].sum()
    dist2['empirical_distr'] = dist2['cuenta'].cumsum()/n2

    ks_df = dist1.join(dist2, how='outer', lsuffix='_1', rsuffix='_2')
    ks_df = ks_df.fillna(method='ffill')
    ks_df['distr_diff'] = ks_df.eval('empirical_distr_1 - empirical_distr_2')
    ks_df['distr_diff'] = ks_df['distr_diff'].abs()
    KS_Statistic = max(ks_df['distr_diff'])
    # ks_info = ks_df[(ks_df['distr_diff'] == KS_Statistic)]

    d_crit = math.sqrt(-0.5 * math.log(significance_level / 2)) * math.sqrt((n1 + n2) / (n1 * n2))
    return print('Samples come from the same distribution: ' + str(KS_Statistic < d_crit))
