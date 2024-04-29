import anvil.server
from psycopg2 import pool
import psycopg2
import logging

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def say_hello(name):
  dbPool = connectDB('db_config.json')
  connection = dbPool.getconn()
  cursor = connection.cursor()
  cursor.execute(f'INSERT INTO public.test_table (test_field) VALUES ({name})')
  logging.debug(cursor.query)
  connection.commit()
  return 42

def connectDB(config_file):
    # Load database connection settings from config file
    with open(config_file, 'r') as f:
        config = json.load(f)

        # Extract connection settings
        db_host = config['host']
        db_port = config['port']
        db_name = config['database']
        db_user = config['user']
        db_password = config['password']
        db_options = config['options']

        try:
            postgreSQLPool = psycopg2.pool.SimpleConnectionPool(1, 20, user=db_user,
                                                                password=db_password,
                                                                host=db_host,
                                                                port=db_port,
                                                                database=db_name,
                                                                options=db_options)
            logging.info("Connection pool created successfully.")
            return postgreSQLPool
        except Exception as e:
            logging.error("Error creating connection pool:", e)
            return None