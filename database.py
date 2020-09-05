"""
Author: James Taylor
"""

import pyodbc
import yaml



def main():
    keys = yaml_get(r'config.yaml')
    server = 'LAPTOP-CGRK8PLH'
    database = 'global'
    conn = pyodbc.connect("driver={SQL Server Native Client 11.0};server=" 
                            + keys['server'] + "; database=" + keys['database'] + "; trusted_connection=yes;",
        autocommit=True)
    query = """
    SELECT TOP (1) [ID]
      ,[Country]
      ,[Link]
      ,[Valid]
      FROM [global].[dbo].[Links]
    """
    cursor = conn.execute(query)
    print(list(cursor))
    cursor.close() 


def yaml_get(file):
  with open(r"config.yaml") as f:
    return yaml.full_load(f)

if __name__ == "__main__":
    main()

