import mysql.connector
from mysql.connector import Error

def insert_feedback(message, sentiment):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='zapit',
            port=3307
        )
        cursor = con.cursor()
        query = "INSERT INTO FEEDBACK (message, sentiment) VALUES (%s, %s)"
        cursor.execute(query, (message, sentiment))
        con.commit()
        return 1
    except Error as e:
        print(f" Error inserting feedback: {e}")
        return False
    finally:
        if 'cursor' in locals(): #locals for safe exceution of finally block
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()

def get_all_feedback():
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='zapit',
            port=3307
        )
        cursor = con.cursor()
        query = "SELECT * FROM FEEDBACK"
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f" Error fetching feedback: {e}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()

def get_feedback_by_id(id):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='zapit',
            port=3307
        )
        cursor = con.cursor()
        query = "SELECT * FROM FEEDBACK WHERE id = %s"
        cursor.execute(query, (id,))
        return cursor.fetchone()
    except Error as e:
        print(f" Error fetching feedback by ID: {e}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()

def update_feedback(id, message, sentiment):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='zapit',
            port=3307
        )
        cursor = con.cursor()
        query = "UPDATE FEEDBACK SET message = %s, sentiment = %s WHERE id = %s"
        cursor.execute(query, (message, sentiment, id))
        con.commit()
    except Error as e:
        print(f" Error updating feedback: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()

def delete_feedback(id):
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='zapit',
            port=3307
        )
        cursor = con.cursor()
        query = "DELETE FROM FEEDBACK WHERE id = %s"
        cursor.execute(query, (id,))
        con.commit()
        return cursor.rowcount > 0
    
    except Error as e:
        print(f" Error deleting feedback: {e}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()
