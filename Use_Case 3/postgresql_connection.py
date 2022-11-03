import psycopg2 as pg
import pandas as pd
from configparser import ConfigParser
	
file='config.ini'
config=ConfigParser()
config.read(file)

conn = None
try:
	conn = pg.connect(host = config['postgresql']['hostname'],
			  dbname = config['postgresql']['database'],
			  user = config['postgresql']['username'],
			  password = config['postgresql']['pwd'],
	    		  port = config['postgresql']['port_id'])
	cur = conn.cursor()
	cur.execute('SELECT * FROM '+config['postgresql']['table_name'])
	data = cur.fetchall()
	
	df=pd.DataFrame(data,columns=config['postgresql']['column_name'])
	print(df)
	df.to_csv(config['postgresql']['path']+config['postgresql']['file_name'])
except Exception as error:
	print(error)
finally:
	if conn is not None:    
	    conn.close()

