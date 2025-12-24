import mysql.connector
import os
from dotenv import load_dotenv





class DatabaseService:
    load_dotenv()
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=os.getenv('HOST_NAME'),
            user=os.getenv('USER_NAME'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE')
        )

    @staticmethod
    def get_all_contacts():
        conn = DatabaseService.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def create_contact(first_name,last_name,phone_number):
        conn = DatabaseService.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (first_name,last_name,phone_number) VALUES(%s,%s,%s)",
            (first_name, last_name, phone_number)
        )
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    @staticmethod
    def update_contact(contact_id, first_name, last_name, phone_number):
        conn = DatabaseService.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE contacts SET first_name=%s, last_name=%s, phone_number=%s WHERE id=%s",
            (first_name, last_name, phone_number, contact_id)
        )
        conn.commit()
        updated = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return updated

    @staticmethod
    def delete_contact(contact_id):
        conn = DatabaseService.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM contacts WHERE id=%s",
            (contact_id,)
        )
        conn.commit()
        deleted = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return deleted




