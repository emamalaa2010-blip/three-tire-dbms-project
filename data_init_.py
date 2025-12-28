import mysql.connector

def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="school_db"
        )

        if connection.is_connected():
            print("MySQL connected successfully")
            return connection

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None


