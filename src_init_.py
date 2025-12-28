from data.mysql_db import connect_mysql

def save_excel_data():
    connection = connect_mysql()

    if connection:
        print("Ready to save Excel data to MySQL")
        connection.close()
    else:
        print("MySQL connection failed")


