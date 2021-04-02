import * from mysql.connector
from __future__ import print_function
from datetime import date, datetime, timedelta

class Model:

    def __init__(self, DB_NAME, DB_PASS, DB_USER, ERROR_MESSAGE, STATEMENT, DB_HANDLER):
        #constructor implementing connection variables
        cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
        cursor = cnx.cursor()

        try:
          cnx = mysql.connector.connect(user='scott',
                                        database='employ')
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          elif:
            print(err)
          else:
              cnx.close()

    def query_formula(self, sql):
        #method implementing the formula of your sql query

    def data_binding():
        #method binding the sql query query_formula

    def row_count():
        #method counting the sql result

    def execute(self):
        #method that executes the query query_formula
        cursor.execute(query, (hire_start, hire_end))

    def error_message():
        #method with error message about your query

    def data_row():
        #method with data output after sql query
