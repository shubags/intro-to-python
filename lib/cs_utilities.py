import psycopg2
import pandas as pd
import re


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
